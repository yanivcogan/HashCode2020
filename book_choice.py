class BookChooser:
    def __init__(self, days, scores):
        self.scores = scores
        self.days = days
        self.scanned_books = set()

    def add_library(self, library, day):
