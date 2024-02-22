class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

class BookManager:
    def __init__(self):
        self.books = [
            Book("Python Programming", "John Smith", "2020"),
            Book("Data Science Handbook", "Jane Doe", "2018"),
            Book("Introduction to Algorithms", "Robert Johnson", "2009")
        ]

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("List of Books:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print("Found Books:")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
        else:
            print("Book not found.")

def main():
    book_manager = BookManager()

    while True:
        print("\nBook Management Console Application")
        print("1) Add a new book")
        print("2) View all books")
        print("3) Search for a book by title")
        print("4) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the publication year of the book: ")
            book = Book(title, author, year)
            book_manager.add_book(book)
            print("Book added successfully.")
        elif choice == "2":
            book_manager.show_books()
        elif choice == "3":
            title = input("Enter the title of the book to search: ")
            book_manager.search_book(title)
        elif choice == "4":
            print("Thank you for using the Book Management Console Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
