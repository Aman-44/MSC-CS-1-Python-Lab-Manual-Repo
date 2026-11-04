# Name: Aman Gilani
# Enrollment: 92600565017

# Q.41 Python Program to perform WHOIS lookup

print("Name: Aman Gilani \nEnrollment: 92600565017")

import whois

domain = "google.com"

result = whois.whois(domain)

print("WHOIS Information:")

print(result)