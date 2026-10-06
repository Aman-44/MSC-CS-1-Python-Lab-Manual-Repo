# Name: Aman Gilani
# Enrollment: 92600565017

# Q.21 Python Program to show single inheritance using classes Animal and Dog

print("Name: Aman Gilani \nEnrollment: 92600565017")


class Animal:
    def eat(self):
        print("Animal can eat")


class Dog(Animal):
    def bark(self):
        print("Dog can bark")


dog = Dog()
dog.eat()
dog.bark()