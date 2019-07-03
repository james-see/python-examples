#!/usr/bin/python3
import socks
import socket


def set_socks_default():
    # TOR SETUP GLOBAL Vars
    SOCKS_PORT = 9050  # TOR proxy port that is default from torrc, change to whatever torrc

    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", SOCKS_PORT)
    socket.socket = socks.socksocket

    # Perform DNS resolution through the socket
    def getaddrinfo(*args):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
    socket.getaddrinfo = getaddrinfo
    return "success"


def test_socks():
    assert set_socks_default() == "success"
