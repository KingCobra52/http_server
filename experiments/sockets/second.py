import socket


# changes this function name create_server or somehthing more descriptive
def create_socket(socket):
    http_response_text = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "\r\n"
        "<html><body><h1>Hello from your custom server!</h1></body></html>"
    )

    socket.bind(("127.0.0.1", 8080))

    socket.listen(5)
    print("Server is listening on address 127.0.0.1 / localhost")

    client_socket, client_address = socket.accept()
    print(f"Connection established with {client_address}")

    raw_request = client_socket.recv(1024)
    request_text = raw_request.decode("utf-8")
    client_request_path = request_text.split(" ")[1]
    http_response_text = http_response_text.encode("utf-8")
    client_socket.send(http_response_text)
    client_socket.close()
    return client_request_path


if __name__ == "__main__":
    first_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(create_socket(first_socket))
