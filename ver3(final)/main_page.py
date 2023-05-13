import tkinter as tk
from tkinter import ttk

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Port Scanner and IP Check")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="IP 확인",
                             command=lambda: controller.show_frame("IPPage"))
        button1.pack()

        button2 = ttk.Button(self, text="포트 스캐너",
                             command=lambda: controller.show_frame("ScannerPage"))
        button2.pack()
