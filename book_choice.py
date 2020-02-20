from classes import LibraryScan


class BookChooser:
    def __init__(self, days, scores):
        self.scores = scores
        self.days = days
        self.scanned_books = set()
        self.library_scans = []

    def add_library(self, library, days_to_scan):
        sorted_books = sorted(library.book_ids, key=lambda book_id:self.scores[book_id], reverse=True)
        added_books = 0
        chosen_books = []
        for book_id in sorted_books:
            if book_id in self.scanned_books:
                continue
            else:
                chosen_books.append(book_id)
                self.scanned_books.add(book_id)
                added_books += 1
                if added_books >= days_to_scan:
                    break
        if len(chosen_books) < days_to_scan:
            print (f"WARNING: Library {library.index} has {days_to_scan} days but scanned {len(chosen_books)} books")
        self.library_scans.append(LibraryScan(library, chosen_books))

    def get_scans(self):
        return self.library_scans