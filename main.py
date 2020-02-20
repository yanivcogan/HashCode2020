import time
from classes import *
from outputs.all_files import ALL_FILES
from solver import greedy


def main(solve=lambda l, b, n: []):
    print("---START---")
    for filename in ALL_FILES:
        print("solving " + filename + " ...")
        filename = "inputs/" + filename
        with open(filename) as file:
            lines = file.readlines()
        n_books, n_libraries, n_days = (int(x) for x in lines[0].split(' '))
        book_scores = [int(x) for x in lines[1].split(' ')]
        libraries: List[Library] = []
        for i_library in range(n_libraries):
            line_a = lines[i_library * 2 + 2]
            line_b = lines[i_library * 2 + 3]
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
        sum_scores = sum(sum(book_scores[b] for b in scan.ids_in_order) for scan in solution)
        # print("SCORE:", sum_scores)
        save_solution(filename, solution, sum_scores)
    print("---END---")


def save_solution(filename: str, solution: Solution, score):
    lines = [str(len(solution))]
    for scan in solution:
        lines.append(f"{scan.library.index} {len(scan.ids_in_order)}")
        lines.append(" ".join(str(x) for x in scan.ids_in_order))
    outfilename = "outputs/" + filename[7:9] + str(score) + ".out"
    assert outfilename != filename
    with open(outfilename, "w") as file:
        for line in lines:
            file.write(line + "\n")
    print("-> " + filename[7:9] + str(score))


# def stupid_solve(libraries, book_scores, n_days) -> Solution:
#     return [
#         LibraryScan(libraries[1], [5, 2, 3]),
#         LibraryScan(libraries[0], [0, 1, 2, 3, 4])
#     ]


if __name__ == '__main__':
    main(greedy)
