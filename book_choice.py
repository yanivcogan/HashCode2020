from typing import List, Set

from classes import LibraryScan, Library


class BookChooser:
    def __init__(self, days: int, scores: List[int], days2=None, days3=None, days4=None, days5=None):
        self.days: int = days # stop touching my code
        self.scores: List[int] = scores
        self.scanned_books: Set[int] = set()
        self.library_scans: List[LibraryScan] = []

    def add_library(self, library: Library, days_to_scan: int) -> None:
        sorted_books: List[int] = sorted(library.book_ids,
                                         key=lambda i: self.scores[i],
                                         reverse=True)
        chosen_books: List[int] = []
        needed_books: int = days_to_scan * library.ship_rate
        for book_id in sorted_books:
            if book_id in self.scanned_books:
                continue
            else:
                chosen_books.append(book_id)
                self.scanned_books.add(book_id)
                if len(chosen_books) >= needed_books:
                    break
        if len(chosen_books) < needed_books:
            print(f"WARNING: Library {library.index} has {days_to_scan}"
                  f" days but scanned {len(chosen_books)} books")
        self.library_scans.append(LibraryScan(library, chosen_books))

    def get_scans(self) -> List[LibraryScan]:
        return self.library_scans
