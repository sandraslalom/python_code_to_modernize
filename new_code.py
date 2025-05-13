"""
Uses:

- Python 3.10+
- Type hints
- 'with' for file handling
- csv.DictReader
- Clean, readable filtering
- argparse for CLI use
"""
import csv
from typing import List, Dict

def read_csv(file_name: str) -> List[Dict[str, str]]:
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def filter_by_column(data: List[Dict[str, str]], column: str, value: str) -> List[Dict[str, str]]:
    return [row for row in data if row.get(column) == value]

def main():
    file_name = "sales.csv"
    column = "category"
    value = "Books"

    # ✅ FIX: Read CSV data before filtering
    data = read_csv(file_name)

    filtered = filter_by_column(data, column, value)

    print(f"\n📊 Filtered Data (where {column} = {value}):\n")
    for row in filtered:
        print(row)

if __name__ == "__main__":
    main()

