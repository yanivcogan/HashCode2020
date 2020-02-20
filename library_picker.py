from typing import List, Set
from classes import Library


def pick_library(libraries: List[Library], book_scores: List[int], days_left: int, hist: Set[int] = None) -> Library:
    if hist is None:
        hist = {}
    max_intersect_score = 0
    max_intersect_index = 0
    for i in range(len(libraries)):
        library = libraries[i]
        if library.signup_time >= days_left:
            continue
        score: int = score_set(book_scores, hist.difference(library.book_ids.intersection(hist)))
        if score > max_intersect_score:
            max_intersect_index = i
            max_intersect_score = score
    return libraries[max_intersect_index]


def score_set(book_scores: List[int], book_ids: Set[int]) -> int:
    return sum(book_scores[i] for i in book_ids)
