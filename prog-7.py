#Name: Aman Gilani
#Enrollment: 92600565017

#Q.7 Python program to print the largest element and smallest element in  an array

arr = [23, 5, 89, 45, 12, 7]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element:", largest)
print("Smallest element:", smallest)
