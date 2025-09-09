from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from sqlalchemy import inspect, create_engine
from dotenv import load_dotenv
import os
import traceback
import re

# Load environment variables
load_dotenv()

# Initialize LLM with Hugging Face endpoint for conversational model
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    timeout=300  # 5 minutes timeout
)

# Wrap the LLM in ChatHuggingFace for conversational use
chat_llm = ChatHuggingFace(llm=llm)

# Prompt template for SQL generation (using chat format)
sql_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a SQL expert. Given the following database schema: {schema}. Output *only* the SQL query, enclosed in ```sql and ``` markers, in the following format: each clause (SELECT, FROM, GROUP BY, etc.) on a new line with 4-space indentation, using backticks (`) around column names (e.g., `Column Name`), and capitalizing AS aliases. Example: ```sql
SELECT
    `Sales Channel`,
    SUM(`Total Revenue`) AS Total_Revenue
FROM sales
GROUP BY `Sales Channel`
```; For 'total revenue', output: ```sql
SELECT
    SUM(`Total Revenue`) AS Total_Revenue
FROM sales
```;"""),
    ("user", "User question: {question}")
])

# Function to get schema from the SQLite database
def get_schema(engine):
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    schema = {}
    for table in tables:
        schema[table] = [col['name'] for col in inspector.get_columns(table)]
    return schema

# Function to extract and fix SQL query from response
def extract_sql_query(response_text, schema):
    match = re.search(r'```sql\s*([\s\S]*?)\s*```', response_text, re.DOTALL)
    if match:
        query = match.group(1).strip()
        #print(f"Debug: Raw query before fix: {query}")  # Debug print
        for col in schema.get('sales', []):
            if ' ' in col and col not in query:  # Check for unquoted or mismatched column
                query = query.replace(col.replace(' ', '_'), f'`{col}`')
                #print(f"Debug: Replaced {col.replace(' ', '_')} with `{col}`'")
        # Reformate query to match desired style
        lines = query.split('\n')
        formatted_lines = []
        has_select = False
        for line in lines:
            line = line.strip()
            if line.lower().startswith("select"):
                formatted_lines.append("SELECT")
                has_select = True
            elif line.lower().startswith("from"):
                formatted_lines.append("FROM sales")
            elif line.lower().startswith("group by"):
                formatted_lines.append("    " + line)  # Append as-is with indentation
            elif line:  # Preserve any other non-empty line (e.g., column selections)
                formatted_lines.append("    " + line.replace('"', '`').replace(" as ", " AS "))
        # Add default FROM sales if SELECT is present but FROM is missing
        if has_select and not any(line.lower().startswith("from") for line in lines):
            formatted_lines.append("FROM sales")
        query = "\n".join(formatted_lines) + ";"
        #print(f"Debug: Fixed query: {query}")  # Debug print
        if query.lower().startswith("select"):
            return query
    return None
# Import the SQL executor
from sql_executor import execute_sql_query

# Example chain: Prompt -> LLM (for testing)
simple_chain = sql_prompt | chat_llm

if __name__ == "__main__":
    engine = create_engine('sqlite:///sales.db')
    schema = get_schema(engine)
    print(f"Schema retrieved: {schema}")
    print("\nWelcome to Ask-My-Data! Ask a question about your sales data (e.g., 'Total revenue by region') or type 'exit' to quit.")
    while True:
        user_input = input("\nYour question: ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        if not user_input:
            print("Please enter a question or 'exit'.")
            continue
        try:
            response = simple_chain.invoke({"schema": str(schema), "question": user_input})
            #print(f"Debug: Full response: {response.content}")  # Debug print
            sql_query = extract_sql_query(response_text=response.content, schema=schema)
            if sql_query:
                print(f"\nGenerated SQL:\n  {sql_query}")
                result = execute_sql_query(sql_query)
                if isinstance(result, list):
                    print("\nQuery Results:")
                    if result:
                        # Dynamic headers based on query
                        headers = [col.split(" AS ")[1].strip() if " AS " in col else col.strip() for col in sql_query.split("SELECT")[1].split("FROM")[0].replace("\n", " ").split(",")]
                        # Calculate maximum widths for each column
                        col_widths = [len(headers[i]) for i in range(len(headers))]
                        for row in result:
                            for i, item in enumerate(row):
                                if i < len(col_widths):
                                    col_widths[i] = max(col_widths[i], len(str(item)))
                        # Print header
                        header_str = "  " + " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
                        print(header_str)
                        # Print separator
                        separator = "  " + "-+-".join("-" * width for width in col_widths)
                        print(separator)
                        # Print data rows with conditional numeric formatting
                        for row in result:
                            row_str = "  " + " | ".join(
                                f"{str(item):<{col_widths[i]}}"
                                if i == 0 or not (str(item).replace('.', '').replace('-', '').isdigit() or ('.' in str(item) and str(item).replace('.', '').isdigit()))
                                else f"{float(item):>{col_widths[i]}.2f}"
                                for i, item in enumerate(row) if i < len(col_widths)
                            )
                            print(row_str)
                    else:
                        print("  No results found.")
                else:
                    print("\nExecution Error:")
                    print("  " + result)
            else:
                print("\nNo valid SQL query extracted from the response. Please try a different question.")
        except Exception as e:
            print("\nError occurred:")
            traceback.print_exc()