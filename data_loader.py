import pandas as pd
from sqlalchemy import create_engine

def load_csv_to_sqlite(csv_path, db_path='sqlite:///sales.db'):
    # Read CSV into Pandas DataFrame, parsing date columns
    df = pd.read_csv(csv_path, parse_dates=['Order Date', 'Ship Date'])
    
    # Create SQLite engine
    engine = create_engine(db_path)
    
    # Load DataFrame to SQLite table named 'sales'
    df.to_sql('sales', engine, if_exists='replace', index=False)
    
    print(f"Data loaded from {csv_path} to {db_path}")
    return engine

# Example usage
if __name__ == "__main__":
    load_csv_to_sqlite('sales.csv')