class BookChooser:
    def __init__(self, days, scores):
        self.scores = scores
        self.days = days
        self.scanned_books = set()
        self.chosen_books = {}

    def add_library(self, library, days_to_scan):
        sorted_books = sorted(list(library.book_ids), key=lambda book_id:self.scores[book_id], reverse=True)
        added_books = 0
        for book in sorted_books:
            