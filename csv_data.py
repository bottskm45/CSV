import csv
from datetime import datetime

# Part 1: Reading and Writing CSV Files using csv module

# Task 1: Reading Data from a CSV File
def read_data(file_path):
    try:
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except csv.Error as e:
        print(f"CSV error: {e}")
        return None


# Task 2: Writing Data to a CSV File
def write_data(data, file_path, headers):
    try:
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data)
        print(f"Data successfully written to {file_path}")
    except csv.Error as e:
        print(f"CSV error: {e}")

# Task 3: Data Cleaning and Transformation
def clean_and_transform_data(file_path):
    cleaned_data = []
    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    product  = row['Product'].strip()
                    customer = row['Customer'].strip()
                    sales    = float(row['Sales'].strip())
                    # Parse the date and format it as a string
                    date_obj = datetime.strptime(row['Date'].strip(), '%Y-%m-%d')
                    date_str = date_obj.strftime('%Y-%m-%d %H:%M:%S')

                    cleaned_data.append({
                        'Date': date_str,
                        'Product': product,
                        'Customer': customer,
                        'Sales': sales,
                    })
                except (ValueError, KeyError):
                    continue  # Skip rows with missing or malformatted data
        return cleaned_data
    except FileNotFoundError:
        print("File not found.")
        return None
    except csv.Error as e:
        print(f"CSV error: {e}")
        return None

# Task 4: Data Aggregation and Analysis
def data_aggregation_and_analysis(data):
    total_sales = sum(float(item['Sales']) for item in data)
    average_sales = total_sales / len(data) if data else 0
    max_sale = max(data, key=lambda x: float(x['Sales'])) if data else None
    min_sale = min(data, key=lambda x: float(x['Sales'])) if data else None
    return total_sales, average_sales, max_sale, min_sale


# Task 5: Data Filtering
def filter_and_select_data(file_path, category, min_quantity):
    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            filtered_data = [
                row for row in reader
                if row['Category'] == category and int(row['Quantity']) < min_quantity
            ]
            return filtered_data
    except FileNotFoundError:
        print("File not found.")
        return None
    except csv.Error as e:
        print(f"CSV error: {e}")
        return None
