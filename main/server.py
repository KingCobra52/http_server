import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1', 8080))
socket.listen(5)
print('Server is listening on http://127.0.0.1:8080 ...')

while True:

    try:
    #client_socket is the socket we created to talk to the
        client_socket, client_address = socket.accept()

        raw_request = client_socket.recv(1024)
        request_text = raw_request.decode('utf-8')

        print(f"Received request from {client_address}:\n{request_text}\n")

        path = request_text.split(" ")[1]

        if path == "/":
            status_line = "HTTP/1.1 200 OK"
            response_body = "<html><body><h1>Hello from your custom server!</h1></body></html>"
        elif path == "/about":
            status_line = "HTTP/1.1 200 OK"
            response_body = "<html><body><h1>About Us</h1><p>We built this from scratch!</p></body></html>"
        else:
            status_line = "HTTP/1.1 404 NOT FOUND"
            response_body = "<html><body><h1>404 NOT FOUND</h1></body></html>"

        response_text = (
                f"{status_line}\r\n"
                "Content-Type: text/html\r\n"
                "\r\n"
                f"{response_body}"
            )

        client_socket.send(response_text.encode('utf-8'))
        client_socket.close()

    except Exception as e:
        print(f"Error occured while handling a request: {e}")
