import threading
import socket

#determines response to the client based on the path
#we never see the response ourselves / can't test it through the browser
def determine_response(path):
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

    return response_text

#spawns a new thread for the client_socket
#the new thread will handle decoding the data from the client, crafting a response, and sending the response back to the client
def thread_function(client_socket, client_address):
    raw_request = client_socket.recv(1024)
    request_text = raw_request.decode('utf-8')

    print(f"Received request from {client_address}: \n{request_text}\n")

    path = request_text.split(" ")[1]

    response_text = determine_response(path)

    client_socket.send(response_text.encode('utf-8'))
    client_socket.close()


if __name__ == "__main__":
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind(('127.0.0.1', 8080))
    socket.listen(5) #might not matter due to threading
    print('Server listen on 127.0.0.1, port 8080')

    threads = list()
    while True:
        try:
            client_socket, client_address = socket.accept()
            new_thread = threading.Thread(target=thread_function, args=(client_socket, client_address))
            threads.append(new_thread)
            new_thread.start()

        except Exception as e:
            print(f"Error occured: {e}")
