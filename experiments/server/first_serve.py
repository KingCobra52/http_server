import socket

HOST, PORT = "", 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Listening on port {PORT}")


while True:
    client_connection, client_address = server_socket.accept()
