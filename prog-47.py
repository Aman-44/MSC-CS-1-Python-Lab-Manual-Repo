# Name: Aman Gilani
# Enrollment: 92600565017

# Q.47 Python Program to perform Simple Port Scanning

print("Name: Aman Gilani \nEnrollment: 92600565017")

import socket

target = input("Enter Target IP Address: ")

print("\nScanning Target:", target)

for port in range(1, 1025):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")

    s.close()

print("\nPort Scanning Completed")