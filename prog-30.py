# Name: Aman Gilani
# Enrollment: 92600565017

# Q.30 Python Program to demonstrate the use of regular expression

print("Name: Aman Gilani \nEnrollment: 92600565017")


import re

text = "My enrollment number is 92600565017."

pattern = r"\d+"

result = re.findall(pattern, text)

print("Numbers found in the text:", result)