# Name: Aman Gilani
# Enrollment: 92600565017

# Q.37 Python Program to create Pie Chart

print("Name: Aman Gilani \nEnrollment: 92600565017")

import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "PHP"]

marks = [85, 75, 65, 55]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")

plt.title("Subject Marks Distribution")

plt.show()