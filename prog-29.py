# Name: Aman Gilani
# Enrollment: 92600565017

# Q.29 Python Program to demonstrate the use of various modes of files

print("Name: Aman Gilani \nEnrollment: 92600565017")


# Write mode
file = open("demo.txt", "w")
file.write("This is the first line.\n")
file.close()


# Append mode
file = open("demo.txt", "a")
file.write("This is the second line.\n")
file.close()


# Read mode
file = open("demo.txt", "r")
print("File Content:")
print(file.read())
file.close()