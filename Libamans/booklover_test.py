import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # Add a book and test if it is in `book_list`.
        book_lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_lover.add_book("War of the Worlds", 4)
        self.assertTrue(book_lover.has_read("War of the Worlds"))

    def test_2_add_book(self):
        # Add the same book twice. Test if it's in `book_list` only once.
        book_lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_lover.add_book("War of the Worlds", 4)
        book_lover.add_book("War of the Worlds", 4)
        self.assertEqual(book_lover.num_books_read(), 1)

    def test_3_has_read(self): 
        # Pass a book in the list and test if the answer is `True`.
        book_lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_lover.add_book("The Hobbit", 5)
        self.assertTrue(book_lover.has_read("The Hobbit"))
        
    def test_4_has_read(self): 
        # Pass a book NOT in the list and use `assert False` to test the answer is `True`.
        book_lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertFalse(book_lover.has_read("1984"))

    def test_5_num_books_read(self): 
        # Add some books to the list, and test num_books matches expected.
        book_lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_lover.add_book("Dune", 4)
        book_lover.add_book("Foundation", 5)
        self.assertEqual(book_lover.num_books_read(), 2)

    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating > 3.
        book_lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_lover.add_book("Dune", 4)
        book_lover.add_book("Foundation", 5)
        book_lover.add_book("Starship Troopers", 3)
        fav_books = book_lover.fav_books()
        self.assertTrue((fav_books['book_rating'] > 3).all())

if __name__ == '__main__':
    unittest.main(verbosity=3)
