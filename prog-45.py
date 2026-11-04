# Name: Aman Gilani
# Enrollment: 92600565017

# Q.45 Python Program to find IP address and DNS records using dig command

print("Name: Aman Gilani \nEnrollment: 92600565017")

import subprocess

domain = input("Enter Domain Name: ")

print("\nIP Address of Website:")

subprocess.run(["dig", "+short", domain])

print("\nDNS Records:")

subprocess.run(["dig", domain, "ANY"])