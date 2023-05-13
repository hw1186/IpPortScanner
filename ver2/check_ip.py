import socket
import netifaces

class CheckIP:
    def __init__(self):
        pass

    def get_local_ip(self):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip

    def get_default_gateway(self):
        gws = netifaces.gateways()
        default_gateway = gws['default'][netifaces.AF_INET][0]
        return default_gateway
