#Name: Aman Gilani
#Enrollment: 92600565017

#Q.8 Python program to add two matrix using array and function

#Using array
a= [[1,2,3],[4,5,6],[7,8,9]]
b= [[9,8,7],[6,5,4],[3,2,1]]

for i in range (len (a)):
    for j in range (len(a[0])):
        print(a[i][j]+b[i][j], end=" ")
    print("")

#Using Function
def matrix_addition():
    a= [[1,3,2],[5,4,6],[8,7,9]]   
    b= [[8,9,7],[4,6,5],[3,1,2]]

    for i in range (len (a)):
        for j in range (len(a[0])):
            print(a[i][j]+b[i][j], end=" ")
        print("")

matrix_addition()