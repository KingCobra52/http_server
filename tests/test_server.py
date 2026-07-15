import pytest

from main.server import determine_response

#write a test for determine_response
def test_determine_response():
    response_text = (
            f"HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            f"<html><body><h1>Hello from your custom server!</h1></body></html>"
        )
    assert determine_response("/") == response_text
