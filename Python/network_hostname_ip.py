# Identify your computer hostname and ip address on the local network
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("********************")
print("Hostname: " + hostname)
print("IP: " + ip)
print("********************")
