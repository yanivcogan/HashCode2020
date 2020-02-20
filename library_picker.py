import math
from typing import List, Set, Optional
from classes import Library


def pick_library(remaining_libraries: Set[Library], book_scores: List[int], days_left: int) -> Optional[Library]:
    max_intersect_score = -math.inf
    max_intersect_library = None
    remove_after = set()
    for library in remaining_libraries:
        if library.signup_time >= days_left:
            remove_after.add(library)
            continue
        score: float = float(score_set(book_scores, library.book_ids_remaining, days_left, library.ship_rate, library.signup_time))
        score /= library.signup_time
        if score > max_intersect_score:
            max_intersect_library = library
            max_intersect_score = score
    remaining_libraries.difference_update(remove_after)  # for optimization
    return max_intersect_library


def score_set(book_scores: List[int], book_ids: Set[int], days_left: int, ship_rate: int, signup_time) -> int:
    ordered = sorted(book_ids, key=lambda book: book_scores[book], reverse=True)
    if len(ordered) == 0:
        return 0
    max_book = min(len(ordered) - 1, (days_left - signup_time) * ship_rate)
    ordered = ordered[0:max_book]
    return sum(book_scores[i] for i in ordered)
