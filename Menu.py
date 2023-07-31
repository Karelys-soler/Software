import tkinter as tk

from tkinter import *
from tkinter import ttk



def menu(root):
    menu = tk.Menu(root)
    root.config(menu=menu, width=300, height=300)

    home = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Home", menu=home)

    home.add_command(label="Register")
    home.add_command(label="Delete register")
    home.add_command(label="Exit", command= root.destroy)

    menu.add_cascade(label="About")
    menu.add_cascade(label="Settings")
    menu.add_cascade(label="Help")