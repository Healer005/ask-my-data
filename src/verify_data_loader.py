import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('sales.db')

# Query the first 5 rows to verify
df = pd.read_sql("SELECT * FROM sales LIMIT 5;", conn)
print("First 5 rows of the 'sales' table:")
print(df)

# Optionally, check the total number of rows
row_count = pd.read_sql("SELECT COUNT(*) as total FROM sales;", conn)
print("\nTotal number of rows:", row_count['total'][0])

# Close the connection
conn.close()