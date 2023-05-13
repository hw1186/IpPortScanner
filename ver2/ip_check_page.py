import tkinter as tk
from check_ip import CheckIP

class IPCheckPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="IP Check", font=("Verdana", 16))
        label.pack(pady=10, padx=10)

        self.ip_checker = CheckIP()

        self.local_ip = tk.Label(self, text="Local IP: " + self.ip_checker.get_local_ip())
        self.local_ip.pack(side="top")

        self.default_gateway = tk.Label(self, text="Default Gateway: " + self.ip_checker.get_default_gateway())
        self.default_gateway.pack(side="top")

        button = tk.Button(self, text="메인 페이지로 이동",
                           command=lambda: controller.show_frame("MainPage"), font=("Verdana", 8))
        button.pack()
