from tkinter import *
from src.public.buttons import *


def main():
    # setting up the tkinter window
    root = Tk()
    icon = PhotoImage(file="src/public/assets/vennom_icon.png")
    root.iconphoto(False, icon)
    root.geometry("250x400+300+300")
    root.resizable(0, 0)
    root.title("VENNOM")
    components(root)
    root.mainloop()
