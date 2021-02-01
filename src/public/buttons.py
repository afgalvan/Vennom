from tkinter import Tk, StringVar, Label, Frame, Button, LEFT, GROOVE, SE
from src.public.button_actions import *


def components(root: Tk):
    # TODO: function to find the result
    # the label that shows the result
    data = StringVar()
    lbl = Label(
        root,
        text="Label",
        anchor=SE,
        font=("Verdana", 20),
        textvariable=data,
        background="#ffffff",
        fg="#000000",
    )
    share_data(data, lbl)
    lbl.pack(expand=True, fill="both")
    display_buttons(root)


def display_buttons(root: Tk):
    # the frames section
    btnrow1 = Frame(root)
    btnrow1.pack(expand=True, fill="both")

    btnrow2 = Frame(root)
    btnrow2.pack(expand=True, fill="both")

    btnrow3 = Frame(root)
    btnrow3.pack(expand=True, fill="both")

    # The buttons section
    btnA = Button(
        btnrow1,
        text="A",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_A_clicked,
    )
    btnA.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btnB = Button(
        btnrow1,
        text="B",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_B_clicked,
    )
    btnB.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btnC = Button(
        btnrow1,
        text="C",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_C_clicked,
    )
    btnC.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btn_del = Button(
        btnrow1,
        text="⟵",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_del_clicked,
    )
    btn_del.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    # buttons for frame 2

    btn_dif = Button(
        btnrow2,
        text="-",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_diff_clicked,
    )
    btn_dif.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btn_union = Button(
        btnrow2,
        text="U",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_union_clicked,
    )
    btn_union.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btn_intersect = Button(
        btnrow2,
        text="∩",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_intersection_clicked,
    )
    btn_intersect.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btn_parenth1 = Button(
        btnrow2,
        text="(",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_parenthesis1,
    )
    btn_parenth1.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btn_parenth2 = Button(
        btnrow2,
        text=")",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_parenthesis2,
    )
    btn_parenth2.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    # button for frame 3

    btn7 = Button(
        btnrow3,
        text="AC",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_AC_clicked,
    )
    btn7.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btn8 = Button(
        btnrow3,
        text="Δ",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_delta_clicked,
    )
    btn8.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btn9 = Button(
        btnrow3,
        text="'",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_prim_clicked,
    )
    btn9.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )

    btnresult = Button(
        btnrow3,
        text="=",
        font=("Verdana", 22),
        relief=GROOVE,
        border=0,
        command=btn_result_clicked,
    )
    btnresult.pack(
        side=LEFT,
        expand=True,
        fill="both",
    )
