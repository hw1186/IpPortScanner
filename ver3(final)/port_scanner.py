import socket
import threading

class PortScanner:
    def __init__(self, ip):
        self.ip = ip

    def scan_port(self, port, text_widget):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((self.ip, port))
        if result == 0:
            text_widget.insert("end", f"Port {port} is open\n")
        sock.close()

    def start_scan(self, text_widget):
        for port in range(1, 1025):
            threading.Thread(target=self.scan_port, args=(port, text_widget)).start()
