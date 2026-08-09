#Name: Aman Gilani
#Enrollment: 92600565017

#Q.4 Python program to find factorial of number

num = int(input("Enter the number : "))

fact=1
for i in range (1,num+1):
    fact *= i
print("The factorial of given number is : ",fact)