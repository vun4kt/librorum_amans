import pandas as pd

class BookLover:
    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, 
                 book_list: pd.DataFrame = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name: str, rating: int):
        if not self.has_read(book_name):
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print("Book already exists in the list.")

    def has_read(self, book_name: str) -> bool:
        return any(self.book_list['book_name'] == book_name)


    def num_books_read(self) -> int:
        return self.num_books

    def fav_books(self) -> pd.DataFrame:
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    # Testing the BookLover class
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    # Add more test cases here if needed
