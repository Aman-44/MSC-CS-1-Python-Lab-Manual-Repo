# Name: Aman Gilani
# Enrollment: 92600565017

# Q.31 Python Program to connect Python with MySQL database

print("Name: Aman Gilani \nEnrollment: 92600565017")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if mydb.is_connected():
    print("Database Connected Successfully")

mydb.close()