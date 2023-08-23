# ChatGPT 엑셀 저장.py

import openpyxl
import random
from datetime import datetime, timedelta

# Create a new workbook
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "Sales Data"

# Add headers
headers = ["Product Name", "Price ($)", "Quantity", "Sale Date"]
worksheet.append(headers)

# Generate and add sales data
num_rows = 100
products = ["Laptop", "Smartphone", "Tablet", "TV", "Headphones", "Camera", "Gaming Console", "Smart Watch"]

for _ in range(num_rows):
    product_name = random.choice(products)
    price = round(random.uniform(100, 2000), 2)
    quantity = random.randint(1, 10)
    sale_date = datetime.now() - timedelta(days=random.randint(1, 365))

    row_data = [product_name, price, quantity, sale_date]
    worksheet.append(row_data)

# Save the workbook
file_path = "c:\\work\\sales.xlsx"
workbook.save(file_path)

print(f"Sales data saved to {file_path}")
