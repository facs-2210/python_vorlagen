# Author: Sandro Osterauer
# Version: 1.0

import random
import sqlite3
from faker import Faker

# requirements 
# pip install Faker

# Connect to a SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

drop_table_query = '''
DROP TABLE IF EXISTS employees;
'''

# Define the SQL command to create a table
create_table_query = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    job TEXT,
    salary REAL
);
'''

# Execute the create table query
cursor.execute(drop_table_query)
cursor.execute(create_table_query)

# Commit the changes so far
conn.commit()

# Generate random number of entries (between 20 and 300)
num_entries = random.randint(20, 300)

# Instantiate the Faker object
faker = Faker()

# Insert fake data into the table using batch insert
batch_size = 100
insert_query = '''
INSERT INTO employees (first_name, last_name, age, job, salary)
VALUES (?, ?, ?, ?, ?);
'''
data_to_insert = []

for _ in range(num_entries):
    first_name = faker.first_name()
    last_name = faker.last_name()
    age = random.randint(18, 65)
    job = faker.job()
    salary = round(random.uniform(30000, 100000), 2)
    
    data_to_insert.append((first_name, last_name, age, job, salary))
    
    if len(data_to_insert) >= batch_size:
        cursor.executemany(insert_query, data_to_insert)
        data_to_insert = []

# Insert any remaining data in the batch
if data_to_insert:
    cursor.executemany(insert_query, data_to_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"{num_entries} entries added to the 'employees' table.")