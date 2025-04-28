import pytest
from pandas_data import read_data
import pandas as pd
import tempfile
import os

def test_read_data_success():
    # Create a temporary CSV file for testing
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        temp_file.write("Name,Age,Email\n")
        temp_file.write("John,25,john@example.com\n")
        temp_file.write("Alice,30,alice@example.com\n")
        temp_file.write("Bob,22,bob@example.com\n")

    try:
        data = read_data(temp_file.name)
        assert data is not None

        # Convert the data to a pandas DataFrame for easier comparison
        expected_data = pd.DataFrame({
            'Name': ['John', 'Alice', 'Bob'],
            'Age': [25, 30, 22],
            'Email': ['john@example.com', 'alice@example.com', 'bob@example.com'],
        })

        # Check if the data matches the expected DataFrame
        assert data.equals(expected_data)

    finally:
        os.remove(temp_file.name)

def test_read_data_missing_file():
    # Test for handling missing file
    assert read_data('non_existent_file.csv') is None

# Run the tests
if __name__ == "__main__":
    pytest.main()
