import pytest
from pandas_data import filter_and_select_data
import pandas as pd
import tempfile
import os

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

        # Create a pandas DataFrame from the expected data for easier comparison
        expected_data = pd.DataFrame({
            'Product': ['Product C', 'Product D', 'Product F'],
            'Category': ['Electronics', 'Electronics', 'Electronics'],
            'Quantity': [8, 7, 3],
        })

        # Reset the index for the filtered data DataFrame
        filtered_data.reset_index(drop=True, inplace=True)

        # Check if the filtered data matches the expected DataFrame
        assert filtered_data.equals(expected_data)

    finally:
        os.remove(temp_file.name)

# Run the tests
if __name__ == "__main__":
    pytest.main()
