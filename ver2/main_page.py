import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Port Scanner and IP Cheack", font=("Verdana", 16)) 
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="IP 확인",
                           command=lambda: controller.show_frame("IPCheckPage"), font=("Verdana", 10))
        button.pack()

        button = tk.Button(self, text="포트 스캐너",
                           command=lambda: controller.show_frame("ScannerPage"), font=("Verdana", 10))
        button.pack()
