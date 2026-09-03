#Name: Aman Gilani
#Enrollment: 92600565017

#Q.11 Python Program to demonstrate use of list and various functions of it

print("Name: Aman Gilani \nEnrollment: 92600565017")

numbers = [10, 20, 30, 40, 50]

print("The list is: ", numbers)

numbers.append(60)
print("After append: ", numbers)

numbers.insert(2, 25)
print("After insert: ", numbers)

numbers.remove(40)
print("After remove: ", numbers)

numbers.sort()
print("After sort: ", numbers)

numbers.reverse()
print("After reverse: ", numbers)

print("The length of list is: ", len(numbers))