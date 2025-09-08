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
    ("system", "You are a SQL expert. Given the following database schema: {schema}. Output only the SQL query, enclosed in ```sql and ```."),
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
        # Replace unquoted column names with spaces with quoted versions based on schema
        for col in schema.get('sales', []):
            if ' ' in col:
                quoted_col = f'"{col}"'
                query = query.replace(col, quoted_col)
        # Basic validation to ensure it's a SELECT query
        if query.lower().startswith("select"):
            return query
    return None  # Return None if no valid SQL is found

# Import the SQL executor
from sql_executor import execute_sql_query

# Example chain: Prompt -> LLM (for testing)
simple_chain = sql_prompt | chat_llm

# Example usage with enhanced error handling and execution
if __name__ == "__main__":
    engine = create_engine('sqlite:///sales.db')
    schema = get_schema(engine)
    print(f"Schema retrieved: {schema}")
    try:
        response = simple_chain.invoke({"schema": str(schema), "question": "Total revenue by region"})
        sql_query = extract_sql_query(response.content, schema)
        if sql_query:
            print(f"\nGenerated SQL:\n  {sql_query}")
            # Execute the query
            result = execute_sql_query(sql_query)
            if isinstance(result, list):
                print("\nQuery Results:")
                if result:
                    headers = ["Region", "Total_Revenue"]
                    print("  " + " | ".join(f"{h:<15}" for h in headers))
                    print("  " + "-" * (15 * len(headers) + (len(headers) - 1) * 3))
                    for row in result:
                        print("  " + " | ".join(f"{str(item):<15}" for item in row))
                else:
                    print("  No results found.")
            else:
                print("\nExecution Error:")
                print("  " + result)
        else:
            print("\nNo valid SQL query extracted from the response.")
    except Exception as e:
        print("\nError occurred:")
        traceback.print_exc()  # Print the full stack trace