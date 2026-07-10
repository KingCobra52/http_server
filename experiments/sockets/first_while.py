import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1', 8080))
socket.listen(5)
print('Server is listening on http://127.0.0.1:8080 ...')

while True:
    #client_socket is the socket we created to talk to the
    client_socket, client_address = socket.accept()

    raw_request = client_socket.recv(1024)
    request_text = raw_request.decode('utf-8')

    print(f'Recieved request from {client_address}:\n{request_text}')

    #example valid http response
    response_text = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            "<html><body><h1>Hello from your custom server!</h1></body></html>"
        )

    client_socket.send(response_text.encode('utf-8'))
    client_socket.close()
