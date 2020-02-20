import time
from classes import *
from solver import greedy

ALL_FILES = [
    "a_example.txt",
    "b_read_on.txt",
    "c_incunabula.txt",
    "d_tough_choices.txt",
    "e_so_many_books.txt",
    "f_libraries_of_the_world.txt",
]


def main(solve=lambda l, b, n: []):
    print("---START---")
    for filename in ALL_FILES:
        print("solving " + filename)
        filename = "inputs/" + filename
        with open(filename) as file:
            lines = file.readlines()
        n_books, n_libraries, n_days = (int(x) for x in lines[0].split(' '))
        book_scores = [int(x) for x in lines[1].split(' ')]
        libraries: List[Library] = []
        for i_library in range(n_libraries):
            line_a = lines[i_library + 2]
            line_b = lines[i_library + 3]
            _, signup_time, ship_rate = (int(x) for x in line_a.split(' '))
            book_ids = (int(x) for x in line_b.split(' '))
            libraries.append(Library(
                index=i_library,
                signup_time=signup_time,
                ship_rate=ship_rate,
                book_ids=set(book_ids),
            ))
        t_start = time.time()
        solution = solve(libraries, book_scores, n_days)
        t_end = time.time()
        print("took " + str(t_end - t_start) + " seconds")
        save_solution(filename, solution)
    print("---END---")


def save_solution(filename: str, solution: Solution):
    lines = [str(len(solution))]
    for scan in solution:
        lines.append(f"{scan.library.index} {len(scan.ids_in_order)}")
        lines.append(" ".join(str(x) for x in scan.ids_in_order))
    outfilename = filename.replace(".txt", ".out").replace("inputs", "outputs")
    assert outfilename != filename
    with open(outfilename, "w") as file:
        file.writelines(lines)


# def stupid_solve(libraries, book_scores, n_days) -> Solution:
#     return [
#         LibraryScan(libraries[1], [5, 2, 3]),
#         LibraryScan(libraries[0], [0, 1, 2, 3, 4])
#     ]


if __name__ == '__main__':
    main(greedy)
