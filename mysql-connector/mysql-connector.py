# For questions: @author Noah Denger
# script to connect to mysql database using python
# install module with pip: python -m pip install mysql-connector-python

import mysql.connector

# COMMENTED CODE BELOW IS MYSQL STATEMENT TO CREATE A DATABASE
# CREATE DATABASE profiles;
# USE profiles;
# CREATE TABLE user_profiles (
#     id INT NOT NULL AUTO_INCREMENT,
#     name VARCHAR(255) NOT NULL,
#     gender VARCHAR(10) NOT NULL,
#     country VARCHAR(255) NOT NULL,
#     address VARCHAR(255) NOT NULL,
#     phone_number VARCHAR(20) NOT NULL,
#     email VARCHAR(255) NOT NULL,
#     date_of_birth DATE NOT NULL,
#     PRIMARY KEY (id)
# );

# connect to mysql database
db = mysql.connector.connect(
    host="192.168.174.131", user="root", password="H4_Ker!0", database="profiles"
)



# IF FAKE PROFILES USING FAKER ARE CREATED THEY CAN BE PASTED WITH THE PYTHON CODE BELOW
# insert the profiles into the db
cursor = db.cursor()
for profile in profiles['males']:
    sql = "INSERT INTO user_profiles (name, gender, country, address, phone_number, email, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (profile['name'], profile['sex'], profile['country'], profile['address'], profile['phone'], profile['email'], profile['birthday'])
    cursor.execute(sql, val)
for profile in profiles['females']:
    sql = "INSERT INTO user_profiles (name, gender, country, address, phone_number, email, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (profile['name'], profile['sex'], profile['country'], profile['address'], profile['phone'], profile['email'], profile['birthday'])
    cursor.execute(sql, val)
db.commit()


# create cursor object
mycursor = db.cursor()

# select the first fifty profiles
mycursor.execute("SELECT * FROM user_profiles LIMIT 50")


# TODO: Add to script that you can access all the values separately 

# fetch all rows from the result set
result = mycursor.fetchall()

# print each row
for row in result:
    print(row)
