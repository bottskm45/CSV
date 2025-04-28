import pytest
from csv_data import clean_and_transform_data
import os
import csv
import tempfile

def test_clean_and_transform_data_success():
    # Create a temporary CSV file for testing
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        temp_file.write("Date,Product,Customer,Sales\n")
        temp_file.write("2023-01-01, Product A   , Customer X  , 100.50\n")
        temp_file.write("2023-01-02,   Product B,  Customer Y, 50.25\n")
        temp_file.write("2023-01-03, Product C , Customer Z  , 75.75\n")

    try:
        data = clean_and_transform_data(temp_file.name)
        assert data is not None
        print(data)
        # Test actual values
        assert data == [
            {'Date': '2023-01-01 00:00:00', 'Product': 'Product A', 'Customer': 'Customer X', 'Sales': 100.50},
            {'Date': '2023-01-02 00:00:00', 'Product': 'Product B', 'Customer': 'Customer Y', 'Sales': 50.25},
            {'Date': '2023-01-03 00:00:00', 'Product': 'Product C', 'Customer': 'Customer Z', 'Sales': 75.75}
        ]

    finally:
        os.remove(temp_file.name)


# Run the tests
if __name__ == "__main__":
  pytest.main()
