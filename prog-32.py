# Name: Aman Gilani
# Enrollment: 92600565017

# Q.32 Python Program to create table, insert and display records

print("Name: Aman Gilani \nEnrollment: 92600565017")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS assignment_db")
mycursor.execute("USE assignment_db")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

mycursor.execute("DELETE FROM students")

sql = "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)"

values = [
    (1, "Aman", 22),
    (2, "Rahul", 21),
    (3, "Priya", 23)
]

mycursor.executemany(sql, values)

mydb.commit()

print("Records inserted successfully")

mycursor.execute("SELECT * FROM students")

records = mycursor.fetchall()

print("Student Records:")

for row in records:
    print(row)

mydb.close()