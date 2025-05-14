import csv
from typing import List, Any
import sys
from pathlib import Path


def read_csv(file_name: str) -> List[List[str]]:
    """
    Read data from a CSV file using a context manager.
    
    Args:
        file_name: Path to the CSV file
        
    Returns:
        List of rows from the CSV file
    """
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_name}': {e}")
        sys.exit(1)


def filter_by_column(data: List[List[str]], index: int, value: str) -> List[List[str]]:
    """
    Filter rows based on a column value.
    
    Args:
        data: List of rows to filter
        index: Column index to check
        value: Value to match in the specified column
        
    Returns:
        Filtered list of rows
    """
    return [row for row in data if row[index] == value]


def main() -> None:
    """Main function to process sales data."""
    # Use relative path for better portability
    file_path = Path('sales.csv')
    
    data = read_csv(file_path)
    filtered = filter_by_column(data, 2, 'Books')
    
    print("Filtered Data:")
    for row in filtered:
        print(row)


if __name__ == "__main__":
    main()