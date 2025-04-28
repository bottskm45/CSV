import pytest
from csv_data import write_data
import os
import csv
import tempfile

def test_write_data_success():
    # Create a temporary CSV file for testing
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        temp_file_path = temp_file.name

    try:
        data_to_write = [
            ['Name', 'Age', 'Email'],
            ['John', '25', 'john@example.com'],
            ['Alice', '30', 'alice@example.com'],
            ['Bob', '22', 'bob@example.com']
        ]
        headers = data_to_write[0]

        write_data(data_to_write[1:], temp_file_path, headers)

        # Read and check the written data
        with open(temp_file_path, 'r', newline='') as temp_file:
            csv_reader = csv.reader(temp_file)
            written_data = [row for row in csv_reader]

            # Test actual values
            assert written_data == data_to_write
    finally:
        os.remove(temp_file_path)

# Run the tests
if __name__ == "__main__":
  pytest.main()
