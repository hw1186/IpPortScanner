import tkinter as tk
from tkinter import ttk
from check_ip import CheckIP

class IPPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.ip_checker = CheckIP()
        self.controller = controller

        label = ttk.Label(self, text="IP 확인")
        label.pack(pady=10, padx=10)

        self.local_ip = ttk.Label(self)
        self.local_ip["text"] = "Local IP: " + self.ip_checker.get_local_ip()
        self.local_ip.pack(side="top")

        self.default_gateway = ttk.Label(self)
        self.default_gateway["text"] = "Default Gateway: " + self.ip_checker.get_default_gateway()
        self.default_gateway.pack(side="top")

        self.back = ttk.Button(self, text="Go to Port Scanner", command=self.go_to_port_scanner)
        self.back.pack(side="bottom")

    def go_to_port_scanner(self):
        self.controller.show_frame("ScannerPage")
