# Name: Aman Gilani
# Enrollment: 92600565017

# Q.38 Python Program to create Histogram

print("Name: Aman Gilani \nEnrollment: 92600565017")

import matplotlib.pyplot as plt

marks = [45, 55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.show()