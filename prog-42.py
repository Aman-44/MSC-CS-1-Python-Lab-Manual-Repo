# Name: Aman Gilani
# Enrollment: 92600565017

# Q.42 Python Program to accept domain name and display WHOIS information

print("Name: Aman Gilani \nEnrollment: 92600565017")

import whois

domain = input("Enter Domain Name: ")

result = whois.whois(domain)

print("\nWHOIS Information:")

print("Domain Name:", result.domain_name)

print("Registrar:", result.registrar)

print("Creation Date:", result.creation_date)

print("Expiration Date:", result.expiration_date)