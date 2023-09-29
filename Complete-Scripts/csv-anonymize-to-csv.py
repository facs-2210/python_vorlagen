# Author: Sandro Osterauer
# Version: 1.0

import csv
import json
import sqlite3

# Connect to a SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL command to select data from the employees table
query = '''
SELECT * FROM employees;
'''

# Execute the select query
cursor.execute(query)

# Get all rows
rows = cursor.fetchall()

# Export to CSV
with open('employees.csv', 'w', buffering=8192) as f:
    # Normal Writing
    # Write the header
    f.write("id,first_name,last_name,age,job,salary\n")
    
    # Write each row
    for row in rows:
        f.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n")


# Export to CSV using csv.writer
with open('employees-csv-writer.csv', 'w', newline='', buffering=8192) as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["id", "first_name", "last_name", "age", "job", "salary"])  # Write header

    for row in rows:
        csv_writer.writerow(row)  # Write each row

# Convert row to dictionary
json_data = []
for row in rows:
    json_data.append(dict(zip(["id", "first_name", "last_name", "age", "job", "salary"], row)))

# Export to JSON
with open('employees.json', 'w', buffering=8192) as f:
    json.dump(json_data, f, indent=4)

# Close the connection
conn.close()