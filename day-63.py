# Exercise: Library Class Example (Non-persistent data)

class Library:
    def __init__(self, book_list):
        print(type(book_list))
        # Instance variables
        self.books = book_list
        self.no_of_books = len(book_list)
        

    # Method to display all books
    def show_books(self):
        print("\n📚 Books in Library:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")
        print(f"Total books: {self.no_of_books}")

    # Method to add a new book
    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books = len(self.books)
        print(f'✅ "{book_name}" has been added to the library!')

    # Method to get total number of books
    def get_total_books(self):
        return self.no_of_books


# ------------------------------
# 🧠 MAIN PROGRAM
# ------------------------------
if __name__ == "__main__":
    my_library = Library(["Python Crash Course", "Clean Code", "Think Python"])

    my_library.show_books()        # Show initial books

    my_library.add_book("The Pragmatic Programmer")   # Add new book
    print(f"📖 Total number of books now: {my_library.get_total_books()}")

    my_library.show_books()        # Show updated list

    print("\n💡 Note: When you restart this program, the added book will disappear — because it's not saved to any file or database.")
    