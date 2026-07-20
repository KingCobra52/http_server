import socket
import asyncio
#should be a task on every accept -> that's what acts as threading to respond back to the client

#determines response to the client based on the path
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

#ran as a task -> independently schedulable by the loop
#have to await to get results
async def thread_function(client_socket, client_address):
    loop = asyncio.get_running_loop()
    try:
        raw_request = await loop.sock_recv(client_socket, 1024)
        request_text = raw_request.decode('utf-8')

        print(f"Received request from {client_address}: \n{request_text}\n")

        path = request_text.split(" ")[1]

        response_text = determine_response(path)

        await loop.sock_sendall(client_socket, response_text.encode())

    except Exception as e:
        print(f"Error occured in a task: {e}")
        client_socket.close()
    finally:
        client_socket.close()

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(1000) #might not matter due to threading
    server_socket.setblocking(False)
    print('Server listen on 127.0.0.1, port 8080')

    loop = asyncio.get_running_loop()

    while True:
        try:
            client_socket, client_address = await loop.sock_accept(server_socket)
            client_socket.setblocking(False)
            asyncio.create_task(thread_function(client_socket, client_address))

        except Exception as e:
            print(f"Error occured: {e}")

if __name__ == "__main__":
    asyncio.run(main())
