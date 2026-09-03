#Name: Aman Gilani
#Enrollment: 92600565017

#Q.15 Python Program to demonstrate the use of various arguments which can be passed to functions

print("Name: Aman Gilani \nEnrollment: 92600565017")

def student(name, age=21):
    print("Student Name is: ", name)
    print("Student Age is: ", age)

print("Using positional arguments:")
student("Aman", 21)

print("Using keyword arguments:")
student(age=22, name="Rahul")

print("Using default arguments:")
student("Karan")