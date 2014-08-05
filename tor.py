from stem import process, control, Signal
from urllib2 import urlopen
import socket
import socks
import os


class Tor:

    def __init__(self, port=9080, cont_port=9081):
        self._port, self._cont_port = port, cont_port
        self._tor_process = process.launch_tor_with_config(
            config={'SocksPort': str(port), 'ControlPort': str(cont_port)})
        self._controller = control.Controller.from_port(port=cont_port)
        self._controller.authenticate()
        self.setsocket()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.unsetsocket()
        self._tor_process.terminate()

    def renew(self):
        self._controller.signal(Signal.NEWNYM)

    def ip(self):
        return urlopen('http://icanhazip.com').read().strip()

    def setsocket(self):
        self._real_socket = socket.socket
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', self._port)
        socket.socket = socks.socksocket

    def unsetsocket(self):
        socket.socket = self._real_socket
