# Name: Aman Gilani
# Enrollment: 92600565017

# Q.48 Python Program to generate hash values using hashlib

print("Name: Aman Gilani \nEnrollment: 92600565017")

import hashlib

text = input("Enter a String: ")

md5_hash = hashlib.md5(text.encode()).hexdigest()

sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print("\nMD5 Hash:", md5_hash)

print("SHA256 Hash:", sha256_hash)