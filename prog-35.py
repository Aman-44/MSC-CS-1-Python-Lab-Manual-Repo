# Name: Aman Gilani
# Enrollment: 92600565017

# Q.35 Python Program to demonstrate the use of DataFrames

print("Name: Aman Gilani \nEnrollment: 92600565017")

import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Age": [22, 21, 23],
    "City": ["Ahmedabad", "Rajkot", "Surat"]
}

df = pd.DataFrame(data)

print("Student DataFrame:")

print(df)

print("\nDataFrame Information:")

print(df.info())

print("\nFirst Two Records:")

print(df.head(2))