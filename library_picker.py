import math
from typing import List, Set, Optional
from classes import Library


def pick_library(libraries: List[Library], book_scores: List[int], days_left: int) -> Optional[Library]:
    max_intersect_score = -math.inf
    max_intersect_index = None
    remaining_ids = set()
    for library in libraries:
        for book_id in library.book_ids_remaining:
            remaining_ids.add(book_id)
    average_score = score_set(book_scores, remaining_ids)
    for i in range(len(libraries)):
        library = libraries[i]
        if library.signup_time >= days_left:
            continue
        score: int = score_set(book_scores, library.book_ids_remaining)
        score -= average_score * library.signup_time
        if score > max_intersect_score:
            max_intersect_index = i
            max_intersect_score = score
    if max_intersect_index is None:
        return None
    return libraries[max_intersect_index]


def score_set(book_scores: List[int], book_ids: Set[int]) -> int:
    return sum(book_scores[i] for i in book_ids)
