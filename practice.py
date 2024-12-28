import tkinter as tk
import random

root = tk.Tk()
root.title("A simple random game")
root.geometry("900x450")
label = tk.Label(root, text="Try clicking the button", font=("Lato", 22, "bold"))
label.pack(padx=10, pady=10)

def stop_program():
    new_text = "That's it you can't move the button anymore"
    button.config(text=new_text, command=stay_put)

def stay_put():
    button.place(x=50, y=120)

def on_click():
    button.flash()
    button.place(x=random.randint(0,200), y=random.randint(0,250))

button = tk.Button(root, text="Click me", command=on_click)
on_click()
root.after(10000, stop_program)

root.mainloop()