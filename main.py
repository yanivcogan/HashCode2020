import math

ALL_FILES = [
    "./a_example.in",
    "./b_small.in",
    "./c_medium.in",
    "./d_quite_big.in",
    "./e_also_big.in",
]
OPENED_FILE = ALL_FILES[0]


def main():
    print("---START---")
    data = OPENED_FILE
    with open(data) as file:
        lines = file.readlines()
    first_line_parts = lines[0].split(' ')


if __name__ == '__main__':
    main()
