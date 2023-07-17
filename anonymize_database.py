import sqlite3
import csv
import json

# Connect to the database
conn = sqlite3.connect("database.sqlite3")

# Get the table name from the user
table_name = input("Enter the table name: ")

# Get the data from the table
cur = conn.cursor()
cur.execute("SELECT * FROM {}".format(table_name))
rows = cur.fetchall()

# Anonymize the data
for row in rows:
    for column in row:
        if isinstance(column, str):
            column = column.replace(" ", "_")

# Export the data to CSV or JSON
export_format = input("Export to CSV (c) or JSON (j): ")

if export_format == "c":
    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

elif export_format == "j":
    with open("output.json", "w") as f:
        json.dump(rows, f, indent=4)

conn.close()
