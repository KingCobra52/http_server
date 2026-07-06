import socket


# changes this function name create_server or somehthing more descriptive
def create_socket(socket):
    socket.bind(("127.0.0.1", 8080))

    socket.listen(5)
    print("Server is listening on address 127.0.0.1 / localhost")


if __name__ == "__main__":
    first_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    create_socket(first_socket)
