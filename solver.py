from classes import *
from library_picker import pick_library
from book_choice import BookChooser


def greedy(libraries: List[Library], book_scores: List[int], days_left: int) -> Solution:
    selector = BookChooser(days_left, book_scores)
    print(f"days left: {days_left}")
    selected_indices = set()
    while days_left >= 0:
        selected_library = pick_library(libraries, book_scores, days_left, selector.scanned_books)
        if selected_library is None:
            print(f"ran out of libraries to pick")
            break
        if selected_library.index in selected_indices:
            break
        selected_indices.add(selected_library.index)
        days_left -= selected_library.signup_time
        selector.add_library(selected_library, days_left)
        print(f"picked {selected_library.index}. days left: {days_left}")
    return selector.get_scans()


