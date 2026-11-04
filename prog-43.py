# Name: Aman Gilani
# Enrollment: 92600565017

# Q.43 Python Program to display domain registrar using WHOIS

print("Name: Aman Gilani \nEnrollment: 92600565017")

import whois

domain = input("Enter Domain Name: ")

result = whois.whois(domain)

print("\nDomain Name:", domain)

print("Registrar Name:", result.registrar)