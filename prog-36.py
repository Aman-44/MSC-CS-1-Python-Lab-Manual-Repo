# Name: Aman Gilani
# Enrollment: 92600565017

# Q.36 Python Program to demonstrate different ways of creating DataFrames

print("Name: Aman Gilani \nEnrollment: 92600565017")

import pandas as pd

# Method 1: Using Dictionary

data1 = {
    "Name": ["Aman", "Rahul"],
    "Age": [22, 21]
}

df1 = pd.DataFrame(data1)

print("DataFrame using Dictionary:")

print(df1)


# Method 2: Using List

data2 = [
    ["Aman", 22],
    ["Rahul", 21],
    ["Priya", 23]
]

df2 = pd.DataFrame(data2, columns=["Name", "Age"])

print("\nDataFrame using List:")

print(df2)


# Method 3: Using List of Dictionaries

data3 = [
    {"Name": "Aman", "Age": 22},
    {"Name": "Rahul", "Age": 21}
]

df3 = pd.DataFrame(data3)

print("\nDataFrame using List of Dictionaries:")

print(df3)


# Method 4: Using Series

data4 = {
    "Name": pd.Series(["Aman", "Rahul"]),
    "Age": pd.Series([22, 21])
}

df4 = pd.DataFrame(data4)

print("\nDataFrame using Series:")

print(df4)