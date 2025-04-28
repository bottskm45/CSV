import pytest
from pandas_data import clean_and_transform_data
import pandas as pd
import tempfile
import os

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
        # Convert the expected data to a pandas DataFrame for easier comparison
        expected_data = pd.DataFrame({
            'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
            'Product': ['Product A', 'Product B', 'Product C'],
            'Customer': ['Customer X', 'Customer Y', 'Customer Z'],
            'Sales': [100.50, 50.25, 75.75],
        })

        # Check if the data matches the expected DataFrame
        assert data.equals(expected_data)

    finally:
        os.remove(temp_file.name)

# Run the tests
if __name__ == "__main__":
    pytest.main()
