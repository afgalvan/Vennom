from tkinter import *
from buttons import *

val = ""
A = 0
operator = ""


def components(root):
    # TODO: function to find the result
    # the label that shows the result
    data = StringVar()
    share_data(data)
    lbl = Label(
        root,
        text="Label",
        anchor=SE,
        font=("Verdana", 20),
        textvariable=data,
        background="#ffffff",
        fg="#000000",
    )
    lbl.pack(expand=True, fill="both")
    display_buttons(root)


def main():
    # setting up the tkinter window
    root = Tk()
    icon = PhotoImage(file="vennom.png")
    root.iconphoto(False, icon)
    root.geometry("250x400+300+300")
    root.resizable(0, 0)
    root.title("VENNOM")
    components(root)
    root.mainloop()


if __name__ == "__main__":
    main()
