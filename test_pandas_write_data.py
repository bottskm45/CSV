import pytest
from pandas_data import write_data
import pandas as pd
import tempfile
import os

def test_write_data_success():
    # Create a temporary CSV file for testing
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        temp_file_path = temp_file.name

    try:
        data_to_write = pd.DataFrame({
            'Name': ['John', 'Alice', 'Bob'],
            'Age': [25, 30, 22],
            'Email': ['john@example.com', 'alice@example.com', 'bob@example.com'],
        })

        headers = list(data_to_write.columns)

        write_data(data_to_write, temp_file_path, headers)

        # Read and check the written data
        written_data = pd.read_csv(temp_file_path)

        # Check if the written data matches the expected data
        assert written_data.equals(data_to_write)
    finally:
        os.remove(temp_file_path)

# Run the tests
if __name__ == "__main__":
    pytest.main()
