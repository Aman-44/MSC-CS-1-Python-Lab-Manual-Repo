# Name: Aman Gilani
# Enrollment: 92600565017

# Q.24 Python Program to handle invalid input entered by the user

print("Name: Aman Gilani \nEnrollment: 92600565017")


try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")