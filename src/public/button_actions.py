from src.operations import *
from tkinter import StringVar, Label

data = ""
text = ""
val = ""
A = 0
operator = ""


def share_data(parsed: StringVar, label: Label):
    global data, text
    data = parsed
    text = label


def generic_button(base_button):
    def btn_clicked():
        base_button()
        text.config(fg="black")
        
    return btn_clicked


# function for numerical button clicked
@generic_button
def btn_A_clicked():
    global val, data
    val += "A"
    data.set(val)


@generic_button
def btn_B_clicked():
    global val, data
    val += "B"
    data.set(val)


@generic_button
def btn_C_clicked():
    global val, data
    val += "C"
    data.set(val)


# functions for the operator button click
@generic_button
def btn_diff_clicked():
    global operator, val, data
    operator = "-"
    val += "-"
    data.set(val)


@generic_button
def btn_union_clicked():
    global operator, val, data
    operator = "U"
    val += "U"
    data.set(val)


@generic_button
def btn_intersection_clicked():
    global operator, val, data
    operator = "∩"
    val += "∩"
    data.set(val)


@generic_button
def btn_delta_clicked():
    global operator, val, data
    val += "Δ"
    operator = "Δ"
    data.set(val)


@generic_button
def btn_prim_clicked():
    global operator, val, data
    val += "'"
    operator = "'"
    data.set(val)


@generic_button
def btn_parenthesis1():
    global operator, val, data
    val += "("
    data.set(val)


@generic_button
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


def btn_result_clicked():
    sets = count_sets(val)
    operation = val
    sets_chunk = len(sets)
    print(sets)
    print(val)
    btn_AC_clicked()

    if not is_valid_input(operation) or sets_chunk < 2:
        data.set("Error")
        text.config(fg="red")
    elif sets_chunk == 2:
        two_sets_process(operation, sets)
