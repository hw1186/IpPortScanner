import tkinter as tk

def on_button_click():
    print(entry.get())

window = tk.Tk()
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Print text", command=on_button_click)
button.pack()

window.mainloop()
