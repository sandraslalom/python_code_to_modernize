import csv
from pathlib import Path
import pandas as pd
from typing import List, Any, Optional

def read_csv(file_path: str) -> List[List[Any]]:
    """
    Read data from a CSV file.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        List of rows from the CSV file
    """
    # Using with statement to ensure proper file closure
    data = []
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

def filter_by_column(data: List[List[Any]], index: int, value: Any) -> List[List[Any]]:
    """
    Filter data by a specific column value.
    
    Args:
        data: List of rows to filter
        index: Column index to filter on
        value: Value to filter for
        
    Returns:
        Filtered list of rows
    """
    return [row for row in data if row[index] == value]

def read_with_pandas(file_path: str) -> pd.DataFrame:
    """
    Read CSV file using pandas for more advanced data processing.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        DataFrame containing the CSV data
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV with pandas: {e}")
        return pd.DataFrame()

def main() -> None:
    """Main function to process sales data."""
    # Get the directory of the current script
    file_path = Path('sales.csv')
    
    # Original implementation
    data = read_csv(file_path)
    filtered = filter_by_column(data, 2, 'Books')
    print("Filtered Data:")
    for row in filtered:
        print(row)
    
    # Alternative pandas implementation
    print("\nUsing pandas:")
    df = read_with_pandas(file_path)
    if not df.empty:
        filtered_df = df[df.iloc[:, 2] == 'Books']
        print(filtered_df)

if __name__ == "__main__":
    main()