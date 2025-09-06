from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from sqlalchemy import inspect
from dotenv import load_dotenv
import os
import traceback
import re

# Load environment variables from .env file
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
    ("system", "You are a SQL expert. Given the following database schema: {schema}. Output only the SQL query."),
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

# Function to extract SQL query from response
def extract_sql_query(response_text):
    # Use regex to find the SQL query within ```sql
    match = re.search(r'```sql\n(.*?)```', response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return response_text.strip()  # Fallback to full text if no match

# Example chain: Prompt -> LLM (for testing)
simple_chain = sql_prompt | chat_llm

# Example usage with enhanced error handling
if __name__ == "__main__":
    from data_loader import load_csv_to_sqlite
    engine = load_csv_to_sqlite('sales.csv')
    schema = get_schema(engine)
    print("Schema retrieved:", schema)
    try:
        response = simple_chain.invoke({"schema": str(schema), "question": "Total revenue by region"})
        sql_query = extract_sql_query(response.content)
        print("Generated SQL:", sql_query)
    except Exception as e:
        print("Error occurred:")
        traceback.print_exc()  # Print the full stack trace