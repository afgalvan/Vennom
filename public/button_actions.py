from tkinter import *
from main import val, A, operator

data = ""


def share_data(parsed):
    global data
    data = parsed


# function for numerical button clicked
def btn_A_clicked():
    global val, data
    val += " A "
    data.set(val)


def btn_B_clicked():
    global val, data
    val += " B "
    data.set(val)


def btn_C_clicked():
    global val, data
    val += " C "
    data.set(val)


# functions for the operator button click
def btn_diff_clicked():
    global operator, val, data
    operator = "-"
    val += "-"
    data.set(val)


def btn_union_clicked():
    global operator, val, data
    operator = "U"
    val += "U"
    data.set(val)


def btn_intersection_clicked():
    global operator, val, data
    operator = "∩"
    val += "∩"
    data.set(val)


def btn_delta_clicked():
    global operator, val, data
    val += "Δ"
    operator = "Δ"
    data.set(val)


def btn_prim_clicked():
    global operator, val, data
    val += "'"
    operator = "'"
    data.set(val)


def btn_parenthesis1():
    global operator, val, data
    val += "("
    data.set(val)


def btn_parenthesis2():
    global operator, val, data
    val += ")"
    data.set(val)


# Calculator special buttons
def btn_AC_clicked():
    global operator, val, data
    val = ""
    operator = ""
    data.set(val)


def btn_del_clicked():
    global operator, val, data
    if len(val):
        data.set("")
        val = val[:-1]
        data.set(val)
    else:
        pass
