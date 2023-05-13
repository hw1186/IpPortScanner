import socket
import netifaces

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_default_gateway():
    gws = netifaces.gateways()
    default_gateway = gws['default'][netifaces.AF_INET][0]
    return default_gateway

local_ip = get_local_ip()
default_gateway = get_default_gateway()

print(f"Local IP: {local_ip}")
print(f"Default Gateway: {default_gateway}")
