import pytest
from csv_data import data_aggregation_and_analysis

def test_data_aggregation_and_analysis_success():
    data = [
        {
            'Date': '2023-01-01',
            'Product': 'Product A',
            'Customer': 'Customer X',
            'Sales': '100.50'
        },
        {
            'Date': '2023-01-02',
            'Product': 'Product B',
            'Customer': 'Customer Y',
            'Sales': '50.25'
        },
        {
            'Date': '2023-01-03',
            'Product': 'Product C',
            'Customer': 'Customer Z',
            'Sales': '75.75'
        }
    ]
    total_sales, average_sales, max_sale, min_sale = data_aggregation_and_analysis(data)
    print(total_sales, average_sales, max_sale, min_sale)
    # Test actual values
    assert total_sales == 226.50
    assert average_sales == 75.50
    assert max_sale == {
        'Date': '2023-01-01',
        'Product': 'Product A',
        'Customer': 'Customer X',
        'Sales': '100.50'
    }
    assert min_sale == {
        'Date': '2023-01-02',
        'Product': 'Product B',
        'Customer': 'Customer Y',
        'Sales': '50.25'
    }


# Run the tests
if __name__ == "__main__":
  pytest.main()
