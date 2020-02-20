

class Library:
    def __init__(self, index: int, signup_time: int, ship_rate: int, book_ids: Set[int]):
        self.index = index
        self.signup_time = signup_time
        self.ship_rate = ship_rate  # in books per day
        self.book_ids = book_ids

class Solution:
    pass