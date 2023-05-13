import tkinter as tk

def on_menu_item_click():
    print("Menu item clicked!")

window = tk.Tk()

menu = tk.Menu(window)
window.config(menu=menu)

sub_menu = tk.Menu(menu)
menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="Item", command=on_menu_item_click)

window.mainloop()
