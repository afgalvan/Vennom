from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles, venn2, venn2_circles
from re import fullmatch, findall
from subprocess import call
from platform import system

OS = system()
zones3 = ("100", "110", "111", "010", "101", "001", "011")
zones2 = (
    "100",
    "110",
    "010",
)


def clear() -> None:
    """Clear the terminal using the platform module to detect the
    environment."""

    if OS == "Windows":
        call("cls", shell=True)
    else:
        call("clear")


def two_sets_process(user_input: str, sets: dict) -> None:
    """Manage all the methods and functions to make operations with two
    sets to show the graphic result."""

    plt.title(user_input)
    set_names = list(sets.keys())
    set_names.sort()
    set_zones = {}
    set_zones[set_names[0]] = {"100", "110"}
    set_zones[set_names[1]] = {"110", "010"}

    user_input = user_input.replace("(", "")
    user_input = user_input.replace(" ", "")
    divided_equation = user_input.split(")")

    elements = findall("[ABCU\∩\-'\Δ]+?", user_input)
    elements_chunk = len(elements)
    for i in elements:
        if i in "ABC":
            set_result = set_zones[i]
            break
    for i in range(elements_chunk):
        if elements[i] in "ABC" and i + 1 < elements_chunk:
            if elements[i + 1] == "-":
                set_result = set_result - set_zones[elements[i + 2]]
            elif elements[i + 1] == "U":
                set_result = set_result.union(set_zones[elements[i + 2]])
            elif elements[i + 1] == "∩":
                set_result = set_result.intersection(set_zones[elements[i + 2]])
            elif elements[i + 1] == "Δ":
                set_result = set_result.symmetric_difference(set_zones[elements[i + 2]])

    v = venn2(subsets=(1, 1, 1), set_labels=(set_names[0], set_names[1]))
    for i in zones2:
        v.get_patch_by_id(i).set_color("white")
        v.get_label_by_id(i).set_text("")

    c = venn2_circles(subsets=(1, 1, 1))
    for i in range(len(c)):
        c[i].set_lw(1.0)
        c[i].set_ls("solid")

    for i in set_result:
        v.get_patch_by_id(i).set_color("red")

    plt.show()


def count_sets(user_input: str) -> dict:
    """Count the sets quantity given by the user and return
    a dictionary with the count of each one"""

    sets = {}
    for each in user_input:
        if each in "ABC":
            sets[each] = sets.get(each, 0) + 1
    return sets


def is_ordered(user_input: str) -> bool:
    """Check if the equation entered have a logic order
    such as "a - b" """

    elements = findall("[ABCU\∩\-'\Δ\)\(]+?", user_input)
    elements_chunk = len(elements)
    if fullmatch("[U\∩\-'\Δ]+", elements[0]):
        return False
    if fullmatch("[U\∩\-'\Δ]+", elements[-1]):
        return False
    for i in range(elements_chunk):
        if elements[i] in "ABC" and i + 1 != len(elements):
            if not fullmatch("[U\∩\-'\Δ\)\(]+", elements[i + 1]):
                return False
        elif elements[i] in "U\∩\-'\Δ" and i + 1 != len(elements):
            if elements[i + 1] not in "ABC()" and i + 1 != len(elements):
                return False
    return True


def is_valid_input(user_input: str) -> bool:
    """Ask the user the equation and validate that only enter allowed
    variables, set names and operations"""

    if not user_input.replace(" ", ""):
        print("Error. empty")
        return False
    elif not fullmatch("[\ ABCU\∩\-'\Δ\)\(]+", user_input):
        print("Error. not in list")
        return False
    elif not is_ordered(user_input):
        print("Error. unordered")
        return False
    return True


def cli_input() -> tuple:
    valid_input = True

    #  clear()
    while not valid_input:
        user_input = input("\nIngrese la ecuación: ")
        user_input = user_input.upper()
        invalid_input = is_valid_input(user_input)

    sets = count_sets(user_input)
    return user_input, sets


def main() -> None:
    while True:
        user_input, sets = cli_input()
        sets_chunk = len(sets)
        if sets_chunk == 2:
            two_sets_process(user_input, sets)


if __name__ == "__main__":
    main()
