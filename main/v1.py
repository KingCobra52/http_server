import socket
from concurrent.futures import ThreadPoolExecutor

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
    try:
        raw_request = client_socket.recv(1024)
        request_text = raw_request.decode('utf-8')

        print(f"Received request from {client_address}: \n{request_text}\n")

        path = request_text.split(" ")[1]

        response_text = determine_response(path)

        client_socket.send(response_text.encode('utf-8'))

        client_socket.close()

    except Exception as e:
        print(f"Error occured in a thread: {e}")
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(1000) #might not matter due to threading
    print('Server listen on 127.0.0.1, port 8080')

    pool_executor = ThreadPoolExecutor(max_workers=32)

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            #use ThreadPool executor with .submit to speed up threading instead of having to spawn new_thread everytime
            # 32 workers max, rest of requests have to be put in a quene that automatically spawns
            pool_executor.submit(thread_function, client_socket, client_address)

        except Exception as e:
            print(f"Error occured: {e}")
            pool_executor.shutdown(wait=True)

if __name__ == "__main__":
    main()
