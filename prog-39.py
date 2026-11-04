# Name: Aman Gilani
# Enrollment: 92600565017

# Q.39 Python Program to create Bar Graph

print("Name: Aman Gilani \nEnrollment: 92600565017")

import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "PHP"]

marks = [85, 75, 65, 55]

plt.bar(subjects, marks)

plt.title("Student Marks")

plt.xlabel("Subjects")

plt.ylabel("Marks")

plt.show()