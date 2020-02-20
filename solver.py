from typing import Dict

from classes import *
from library_picker import pick_library
from book_choice import BookChooser


def greedy(libraries: List[Library], book_scores: List[int], days_left: int) -> Solution:
    # optimization:
    # instead of working with a hist set that is constantly being intersected,
    # each library remembers set of remaining book ids
    # when picking a library, only update remaining book ids
    #   for other libraries that share those books
    libraries_by_book: Dict[int, List[Library]] = {i: [] for i in range(len(book_scores))}
    for library in libraries:
        for book_id in library.book_ids:
            libraries_by_book[book_id].append(library)

    selector = BookChooser(days_left, book_scores)
    selected_indices = set()
    while days_left >= 0:
        selected_library = pick_library(libraries, book_scores, days_left)
        if selected_library is None:
            print(f"ran out of libraries to pick")
            break
        if selected_library.index in selected_indices:
            break
        selected_indices.add(selected_library.index)
        days_left -= selected_library.signup_time
        selector.add_library(selected_library, days_left)
        for book_id in selected_library.book_ids_remaining.copy():
            for library in libraries_by_book[book_id]:
                library.book_ids_remaining.remove(book_id)
    return selector.get_scans()
