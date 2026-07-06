import socket

from sockets.second import create_socket


def test_create_socket():
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    assert create_socket(a_socket) == "some value"
