import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from port_scanner import PortScanner
import ipaddress

class ScannerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Network Port Scanner", font=("Verdana", 16))
        label.pack(pady=10, padx=10)

        self.ip_entry = tk.Entry(self)
        self.ip_entry.pack()
        self.text_area = scrolledtext.ScrolledText(self)
        self.text_area.pack()

        self.scan_button = tk.Button(self, text="스캔 시작", command=self.start_scan, font=("Verdana", 10))
        self.scan_button.pack()

        self.scan_again_button = tk.Button(self, text="다시 스캔", command=self.scan_again, state=tk.DISABLED, font=("Verdana", 10))
        self.scan_again_button.pack()

        button = tk.Button(self, text="매인 페이지로 이동",
                           command=lambda: controller.show_frame("MainPage"), font=("Verdana", 8))
        button.pack()

    def is_valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    def start_scan(self):
        ip = self.ip_entry.get()
        if not self.is_valid_ip(ip):
            messagebox.showwarning("Invalid IP Address", "입력한 IP 주소가 잘못되었습니다..")
            return
        self.scan_button.config(state=tk.DISABLED)
        self.scan_again_button.config(state=tk.DISABLED)
        self.text_area.insert("end", f"Scanning {ip}...\n")
        scanner = PortScanner(ip)
        scanner.start_scan(self.text_area)
        self.after(5000, self.finish_scan) 

    def finish_scan(self):
        self.text_area.insert("end", "스캔이 종료되었습니다.\n")
        self.scan_button.config(state=tk.NORMAL)
        self.scan_again_button.config(state=tk.NORMAL)

    def scan_again(self):
        self.text_area.delete('1.0', tk.END)
        self.ip_entry.delete(0, tk.END)
        self.scan_button.config(state=tk.NORMAL)
        self.scan_again_button.config(state=tk.DISABLED)
