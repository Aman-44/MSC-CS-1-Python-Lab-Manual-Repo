# Name: Aman Gilani
# Enrollment: 92600565017

# Q.46 Python Program to detect emails using Regular Expressions

print("Name: Aman Gilani \nEnrollment: 92600565017")

import re

text = input("Enter Text: ")

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.findall(pattern, text)

print("\nEmail Addresses Found:")

print(result)