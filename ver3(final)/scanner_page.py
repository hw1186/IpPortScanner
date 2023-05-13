import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk
from port_scanner import PortScanner
import ipaddress

class ScannerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.port_scanner = None

        label = ttk.Label(self, text="Port Scanner")
        label.pack(pady=10, padx=10)

        self.ip_entry = ttk.Entry(self)
        self.ip_entry.pack()

        self.start_button = ttk.Button(self, text="스캔 시작", command=self.start_scan)
        self.start_button.pack()

        self.rescan_button = ttk.Button(self, text="다시 스캔", command=self.rescan)
        self.rescan_button.pack()
        self.rescan_button['state'] = 'disable' 

        self.scroll_text = scrolledtext.ScrolledText(self)
        self.scroll_text.pack()

        self.back = ttk.Button(self, text="메인 페이지", command=self.back_to_main)
        self.back.pack(side="bottom")

    def start_scan(self):
        ip = self.ip_entry.get()
        try:
            ipaddress.ip_address(ip)
            self.port_scanner = PortScanner(ip)
            self.port_scanner.start_scan(self.scroll_text)
            self.rescan_button['state'] = 'normal' 
        except ValueError:
            messagebox.showerror("Error", "잘못된 IP 주소 입니다.")

    def rescan(self):
        self.scroll_text.delete('1.0', tk.END)
        self.start_scan()

    def back_to_main(self):
        self.controller.show_frame("MainPage")
