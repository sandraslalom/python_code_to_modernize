#!/usr/bin/env python3
"""
Modernized CSV processing script.

This module provides functionality to read and filter CSV data using modern Python 3 practices.
It includes proper error handling, type hints, and follows PEP 8 conventions.
"""

import csv
import logging
from pathlib import Path
from typing import List, Optional, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def read_csv(file_path: Union[str, Path], encoding: str = 'utf-8') -> List[List[str]]:
    """
    Read CSV file and return data as a list of lists.
    
    Args:
        file_path: Path to the CSV file
        encoding: File encoding (default: utf-8)
        
    Returns:
        List of lists containing CSV data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        csv.Error: If there's an error parsing the CSV
        UnicodeDecodeError: If there's an encoding error
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    try:
        with file_path.open('r', encoding=encoding, newline='') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            logger.info(f"Successfully read {len(data)} rows from {file_path}")
            return data
    except UnicodeDecodeError as e:
        logger.error(f"Encoding error reading {file_path}: {e}")
        raise
    except csv.Error as e:
        logger.error(f"CSV parsing error: {e}")
        raise


def filter_by_column(data: List[List[str]], column_index: int, target_value: str) -> List[List[str]]:
    """
    Filter CSV data by a specific column value.
    
    Args:
        data: List of lists containing CSV data
        column_index: Index of the column to filter by (0-based)
        target_value: Value to filter for
        
    Returns:
        Filtered list of lists
        
    Raises:
        IndexError: If column_index is out of range
        ValueError: If data is empty
    """
    if not data:
        logger.warning("No data provided for filtering")
        return []
    
    if column_index < 0:
        logger.error(f"Invalid column index: {column_index}")
        raise ValueError("Column index must be non-negative")
    
    # Check if column index is valid for the data
    if data and column_index >= len(data[0]):
        logger.error(f"Column index {column_index} out of range for data with {len(data[0])} columns")
        raise IndexError(f"Column index {column_index} is out of range")
    
    try:
        filtered_data = [row for row in data if len(row) > column_index and row[column_index] == target_value]
        logger.info(f"Filtered {len(filtered_data)} rows matching '{target_value}' in column {column_index}")
        return filtered_data
    except Exception as e:
        logger.error(f"Error filtering data: {e}")
        raise


def print_data(data: List[List[str]], title: str = "Data") -> None:
    """
    Print CSV data in a formatted way.
    
    Args:
        data: List of lists containing CSV data
        title: Title to display before the data
    """
    print(f"\n{title}:")
    print("-" * len(title))
    
    if not data:
        print("No data to display")
        return
    
    for i, row in enumerate(data):
        print(f"{i+1:3d}: {', '.join(row)}")


def main() -> None:
    """
    Main function to demonstrate CSV reading and filtering.
    """
    try:
        # Configuration
        csv_file = 'sales.csv'
        filter_column = 2  # Column index for filtering (0-based)
        filter_value = 'Books'
        
        logger.info("Starting CSV processing")
        
        # Read CSV data
        data = read_csv(csv_file)
        
        if not data:
            logger.warning("No data found in CSV file")
            return
        
        # Display original data
        print_data(data, "Original Data")
        
        # Filter data
        filtered_data = filter_by_column(data, filter_column, filter_value)
        
        # Display filtered data
        print_data(filtered_data, f"Filtered Data (Column {filter_column} = '{filter_value}')")
        
        logger.info("CSV processing completed successfully")
        
    except FileNotFoundError as e:
        logger.error(f"File error: {e}")
        print(f"Error: {e}")
    except (csv.Error, UnicodeDecodeError, IndexError, ValueError) as e:
        logger.error(f"Processing error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
