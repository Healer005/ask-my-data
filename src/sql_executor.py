from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create a connection to the SQLite database
engine = create_engine('sqlite:///sales.db')

def execute_sql_query(sql_query):
    """
    Execute a SQL query against the sales.db database and return the results.
    
    Args:
        sql_query (str): The SQL query to execute.
    
    Returns:
        list: List of rows (tuples) from the query result, or an error message if execution fails.
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))
            rows = result.fetchall()
            return rows
    except Exception as e:
        return f"Error executing query: {str(e)}"

if __name__ == "__main__":
    # Example usage (for testing)
    sample_query = "SELECT Region, SUM(Total Revenue) as Total_Revenue FROM sales GROUP BY Region"
    result = execute_sql_query(sample_query)
    if isinstance(result, list):
        for row in result:
            print(row)
    else:
        print(result)