from typing import List, Set, Optional
from classes import Library


def pick_library(remaining_libraries: Set[Library], book_scores: List[int], days_left: int) -> Optional[Library]:
    max_intersect_score = 0
    max_intersect_library = None
    remove_after = set()
    for library in remaining_libraries:
        if library.signup_time >= days_left:
            remove_after.add(library)
            continue
        score: int = score_set(book_scores, library.book_ids_remaining)
        if score > max_intersect_score:
            max_intersect_library = library
            max_intersect_score = score
    remaining_libraries.difference_update(remove_after)  # for optimization
    return max_intersect_library


def score_set(book_scores: List[int], book_ids: Set[int]) -> int:
    return sum(book_scores[i] for i in book_ids)
