from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles, venn2, venn2_circles
from re import fullmatch, findall
from subprocess import call
from platform import system

OS = system()
zones3 = ("100", "110", "111", "010", "101", "001", "011")
zones2 = ("100", "110", "010",)


def clear():
    """Clear the terminal using the platform module to detect the
    enviroment."""
    if OS == "Windows":
        call("cls", shell=True)
    else:
        call("clear")


def two_sets_process(user_input, sets):
    """Manage all the methods and functions to make operations with two
    sets to show the graphic result."""
    set_names = list(sets.keys())
    set_names.sort()
    set_zones = {}
    set_zones[set_names[0]] = {"100", "110"}
    set_zones[set_names[1]] = {"110", "010"}

    v = venn2(subsets=(1, 1, 1), set_labels=(set_names[0], set_names[1]))
    for i in zones2:
        v.get_patch_by_id(i).set_color("white")
        v.get_label_by_id(i).set_text("")

    c = venn2_circles(subsets=(1, 1, 1))
    for i in range(len(c)):
        c[i].set_lw(1.0)
        c[i].set_ls("solid")

    plt.show()


def count_sets(user_input):
    """Count the sets quantity given by the user and return
    a dictionary with the count of each one"""
    sets = {}
    for each in user_input:
        if each in "ABC":
            sets[each] = sets.get(each, 0) + 1
    return sets


def is_ordered(user_input):
    """Check if the equation entered have a logic order
    such as "a - b" """
    elements = findall("[ABCU\∩\-\'\∆\)\(]+?", user_input)
    elements_chunk = len(elements)
    if fullmatch("[U\∩\-\'\∆]+", elements[0]):
        return False
    for i in range(elements_chunk):
        if elements[i] in "ABC" and i+1 != len(elements):
            if not fullmatch("[U\∩\-\'\∆\)\(]+", elements[i+1]):
                return False
    return True


def validate_input():
    """Ask the user the equation and validate that only enter allowed
    variables, set names and operations"""
    #  clear()
    while True:
        user_input = input("\nIngrese la ecuación: ")
        user_input = user_input.upper()
        if not fullmatch("[\ ABCU\∩\-\'\∆\)\(]+", user_input):
            print("Error")
            continue
        if not is_ordered(user_input):
            print("Error")
            continue
        break
    sets = count_sets(user_input)
    sets_chunk = len(sets)

    if sets_chunk == 2:
        two_sets_process(user_input, sets)


def main():
    validate_input()

if __name__ == "__main__":
    main()
