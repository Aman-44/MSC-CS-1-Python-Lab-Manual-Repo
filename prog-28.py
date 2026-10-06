# Name: Aman Gilani
# Enrollment: 92600565017

# Q.28 Python Program to demonstrate the use of file handling

print("Name: Aman Gilani \nEnrollment: 92600565017")


file = open("student.txt", "w")

file.write("Name: Aman Gilani\n")
file.write("Enrollment: 92600565017\n")

file.close()


file = open("student.txt", "r")

content = file.read()

print("\nFile Content:")
print(content)

file.close()