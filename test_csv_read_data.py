import pytest
from csv_data import read_data
import os
import csv
import tempfile

def test_read_data_success():
    # Create a temporary CSV file for testing
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        temp_file.write("Name, Age, Email\n")
        temp_file.write("John, 25, john@example.com\n")
        temp_file.write("Alice, 30, alice@example.com\n")
        temp_file.write("Bob, 22, bob@example.com\n")

    try:
        data = read_data(temp_file.name)
        assert data is not None

        # Test actual values
        assert data[0] == ['Name', ' Age', ' Email']
        assert data[1] == ['John', ' 25', ' john@example.com']
        assert data[2] == ['Alice', ' 30', ' alice@example.com']
        assert data[3] == ['Bob', ' 22', ' bob@example.com']

    finally:
        os.remove(temp_file.name)

def test_read_data_missing_file():
    # Test for handling missing file
    assert read_data('non_existent_file.csv') == None

# Run the tests
if __name__ == "__main__":
    pytest.main()
