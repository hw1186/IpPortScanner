from check_ip import CheckIP
import tkinter as tk


class ipGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.ip_checker = CheckIP()

        self.local_ip = tk.Label(self)
        self.local_ip["text"] = "Local IP: " + self.ip_checker.get_local_ip()
        self.local_ip.pack(side="top")

        self.default_gateway = tk.Label(self)
        self.default_gateway["text"] = "Default Gateway: " + self.ip_checker.get_default_gateway()
        self.default_gateway.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.back = tk.Button(self, text="Go to Port Scanner", command=self.go_to_port_scanner)
        self.back.pack(side="bottom")

    def go_to_port_scanner(self):
        pass
