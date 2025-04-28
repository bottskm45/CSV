import pandas as pd

# Part 2: Reading and Writing CSV Files using pandas module

# Task 1: Reading Data from a CSV File using pandas
def read_data(file_path):
    try:
        # read the file into a DataFrame
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except pd.errors.ParserError as e:
        print(f"Parser error: {e}")
        return None

# Task 2: Writing Data to a CSV File
def write_data(data, file_path, headers):
    try:
        # build a DataFrame from the raw data + headers
        df = pd.DataFrame(data, columns=headers)
        # write it out as CSV (no index column)
        df.to_csv(file_path, index=False)
        print(f"Data successfully written to {file_path}")
    except pd.errors.EmptyDataError as e:
        print(f"Empty data error: {e}")

# Task 3: Data Cleaning and Transformation
def clean_and_transform_data(file_path):
    try:
        # load into pandas
        df = pd.read_csv(file_path)
        # strip spaces
        df['Product']  = df['Product'].str.strip()
        df['Customer'] = df['Customer'].str.strip()
        # clean Sales and convert to float
        df['Sales']    = df['Sales'].astype(str).str.strip().astype(float)
        # parse dates
        df['Date']     = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except pd.errors.ParserError as e:
        print(f"Parser error: {e}")
        return None

# Task 4: Data Aggregation and Analysis using pandas
def data_aggregation_and_analysis(data):
    # data is already a DataFrame
    total_sales   = data['Sales'].sum()
    average_sales = data['Sales'].mean()
    # grab the entire row as a dict
    max_sale = data.loc[data['Sales'].idxmax()]
    min_sale = data.loc[data['Sales'].idxmin()]
    return total_sales, average_sales, max_sale, min_sale

# Task 5: Data Filtering
def filter_and_select_data(file_path, category, min_quantity):
    try:
        df = pd.read_csv(file_path)
        # only keep rows matching the category and with Quantity < min_quantity
        filtered_df = df[(df['Category'] == category) & (df['Quantity'] < min_quantity)]
        return filtered_df
    except FileNotFoundError:
        print("File not found.")
        return None
    except pd.errors.ParserError as e:
        print(f"Parser error: {e}")
        return None
