import socket

response_text = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "\r\n"
    "<html><body><h1>Hello from your custom server!</h1></body></html>"
)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8080))

s.listen(5)
print("Server is listening on http://127.0.0.1:8080")

c_socket, c_address = s.accept()
print(f"Connection established with {c_address}")

raw_request = c_socket.recv(1024)
request_text = raw_request.decode("utf-8")

c_socket.send(response_text.encode("utf-8"))
c_socket.close()
