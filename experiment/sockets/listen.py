#listens to incoming connections from the client servers 
import socket

s = socket.socket()
print("Socket sucessfully created")

# Allow the OS to immediately reuse the port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 12345 

s.bind(('', port))
print(f"socket binded to {port}")

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()

    c.send('Thank you for connecting'.encode())

    print("Connection recived, and to be closed")

    c.close()

    break 