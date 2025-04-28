import pytest
from csv_data import filter_and_select_data
import os
import csv
import tempfile

def test_filter_and_select_data_success():
    # Create a temporary CSV file for testing
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        temp_file.write("Product,Category,Quantity\n")
        temp_file.write("Product A,Electronics,15\n")
        temp_file.write("Product B,Clothing,5\n")
        temp_file.write("Product C,Electronics,8\n")
        temp_file.write("Product D,Electronics,7\n")
        temp_file.write("Product E,Furniture,12\n")
        temp_file.write("Product F,Electronics,3\n")

    try:
        filtered_data = filter_and_select_data(temp_file.name, 'Electronics', 10)
        assert filtered_data is not None

        # Test actual values
        assert len(filtered_data) == 3  # Expecting 2 rows
        assert filtered_data == [
            {'Product': 'Product C', 'Category': 'Electronics', 'Quantity': '8'},
            {'Product': 'Product D', 'Category': 'Electronics', 'Quantity': '7'},
            {'Product': 'Product F', 'Category': 'Electronics', 'Quantity': '3'}
          ]

    finally:
        os.remove(temp_file.name)


# Run the tests
if __name__ == "__main__":
  pytest.main()
