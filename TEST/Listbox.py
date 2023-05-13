import tkinter as tk

def on_button_click():
    print(listbox.get(listbox.curselection()))

window = tk.Tk()
listbox = tk.Listbox(window)
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")
listbox.pack()

button = tk.Button(window, text="Print selection", command=on_button_click)
button.pack()

window.mainloop()
