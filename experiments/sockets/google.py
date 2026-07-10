#connect to google using socket programming
import socket 
import sys 

port = 80 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as e:
    print("There was an error in creating the socket")

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()


if s and host_ip:
    s.connect((host_ip, port))

    print("the socket has successfully connected to google")



