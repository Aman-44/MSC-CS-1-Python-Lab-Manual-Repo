# Name: Aman Gilani
# Enrollment: 92600565017

# Q.44 Python Program to display domain creation date using WHOIS

print("Name: Aman Gilani \nEnrollment: 92600565017")

import whois

domain = input("Enter Domain Name: ")

result = whois.whois(domain)

print("\nDomain Name:", domain)

print("Creation Date:", result.creation_date)