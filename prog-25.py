# Name: Aman Gilani
# Enrollment: 92600565017

# Q.25 Python Program to use try-except-else block

print("Name: Aman Gilani \nEnrollment: 92600565017")


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

else:
    print("Division successful.")
    print("Result:", result)