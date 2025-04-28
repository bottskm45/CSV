import pandas as pd
import pytest
from pandas_data import data_aggregation_and_analysis

def test_data_aggregation_and_analysis_success():
    data = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Product': ['Product A', 'Product B', 'Product C'],
        'Customer': ['Customer X', 'Customer Y', 'Customer Z'],
        'Sales': [100.50, 50.25, 75.75],
    })

    total_sales, average_sales, max_sale, min_sale = data_aggregation_and_analysis(data)

    # Test actual values
    assert total_sales == 226.50
    assert average_sales == 75.50
    assert max_sale.equals(data.iloc[0])  # Check if max_sale DataFrame matches
    assert min_sale.equals(data.iloc[1])  # Check if min_sale DataFrame matches

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
