from typing import Set, List


class Library:
    def __init__(self, index: int, signup_time: int, ship_rate: int, book_ids: Set[int]):
        self.index = index
        self.signup_time = signup_time
        self.ship_rate = ship_rate  # in books per day
        self.book_ids = book_ids


class LibraryScan:
    def __init__(self, library: Library, ids_in_order: List[int]):
        self.library = library
        self.ids_in_order = ids_in_order  # does not have to be all books in library


Solution = List[LibraryScan]
