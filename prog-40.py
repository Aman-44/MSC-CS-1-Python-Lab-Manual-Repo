# Name: Aman Gilani
# Enrollment: 92600565017

# Q.40 Python Program to create Line Graph

print("Name: Aman Gilani \nEnrollment: 92600565017")

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 150, 120, 180, 200]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales Report")

plt.xlabel("Months")

plt.ylabel("Sales")

plt.grid(True)

plt.show()