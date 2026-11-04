# Name: Aman Gilani
# Enrollment: 92600565017

# Q.49 Python Program to check files in a directory using os library

print("Name: Aman Gilani \nEnrollment: 92600565017")

import os

path = input("Enter Directory Path: ")

if os.path.exists(path):

    print("\nFiles in Directory:")

    for file in os.listdir(path):

        if os.path.isfile(os.path.join(path, file)):

            print(file)

else:

    print("Directory does not exist")