from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles, venn2, venn2_circles
from re import fullmatch, findall


def validate_input():
    while True:
        user_input = input("\nIngrese la ecuación: ")
        if not fullmatch("[ABCU]+", user_input):
            print("Error")
            continue
        break


def main():
    pass

if __name__ == "__main__":
    main()
