# simple-port-scanner.py
import socket
import sys

target = input("Enter target IP: ")
ports = range(1, 1025)  # Common ports

print(f"Scanning {target}...")
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} open")
    sock.close()
print("Scan complete.")