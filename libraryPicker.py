from typing import List, Set
from classes import Library


def pickLibrary(libraries: List[Library], bookscores: List[int], days_left: int, hist: Set[int] = None) -> int:
    if hist is None:
        hist = {}
    max_intersect_score = 0
    max_intersect_index = 0
    for i in range(len(libraries)):
        library = libraries[i]
        score: int = score_set(bookscores, library.book_ids & hist)
        if score > max_intersect_score:
            max_intersect_index = i
            max_intersect_score = score
    return max_intersect_index


def score_set(bookscores: List[int], book_ids: Set[int]) -> int:
    return sum(bookscores[i] for i in book_ids)
