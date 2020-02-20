import time
from typing import Set, List
from classes import *

ALL_FILES = [
    "./a_example.in",
    "./b_read_on.in",
    "./c_incunabula.in",
    "./d_tough_choices.in",
    "./e_so_many_books.in",
    "./f_libraries_of_the_world.in",
]


def main(solve=lambda l, b: Solution()):
    print("---START---")
    for filename in ALL_FILES:
        print("solving " + filename)
        with open(filename) as file:
            lines = file.readlines()
        n_books, n_libraries, n_days = (int(x) for x in lines[0].split(' '))
        book_scores = (int(x) for x in lines[0].split(' '))
        libraries: List[Library] = []
        for i_library in range(n_libraries):
            _, signup_time, ship_rate = (int(x) for x in lines[0].split(' '))
            book_ids = (int(x) for x in lines[0].split(' '))
            libraries.append(Library(
                index=i_library,
                signup_time=signup_time,
                ship_rate=ship_rate,
                book_ids=set(book_ids),
            ))
        t_start = time.time()
        solution = solve(libraries, book_scores)
        t_end = time.time()
        print("took " + str(t_end - t_start) + " seconds")
        save_solution(filename, solution)
    print("---END---")


def save_solution(file: str, solution: Solution):
    pass


if __name__ == '__main__':
    main()
