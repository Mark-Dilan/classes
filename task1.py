class Book:
    def __init__(self, title, author, status='available' ):
        self.title = title
        self.author = author
        self.status = status

class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = Book(title, author)
            print(f"Book '{title}' by {author} added to the library.")
        else:
            print(f"Book '{title}' is already in the library.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' removed from the library.")
        else:
            print(f"Book '{title}' not found in the library.")

    def search_book(self, search_term):
        found_books = []
        search_term = search_term.lower()
        for title, book in self.books.items():
         if search_term in book.title.lower() or search_term in book.author.lower():
            found_books.append(book)

        if found_books:
            print(f"Found {len(found_books)} book(s) matching '{search_term}':")
            for book in found_books:
                print(f"  Title: {book.title}, Author: {book.author}")
        else:
           print(f"No books found matching '{search_term}'.")

    def check_book_status(self, title):
        if title in self.books:
         status = self.books[title].status
         print(f"Book '{title}' is {status}.")
        else:
          print(f"Book '{title}' not found in the library.")

    def library_manager(self):
      while True:
            print("Library Menu ")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Search Book")
            print("4. Check Status")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                self.add_book(title, author)
            elif choice == '2':
                title = input("Enter title of book to remove: ")
                self.remove_book(title)
            elif choice == '3':
                search_term = input("Enter title or author to search: ")
                self.search_book(search_term)
            elif choice == '4':
                title = input("Enter title of book to check status: ")
                self.check_book_status(title)
            elif choice == '5':
                print("Exiting Library System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

my_library = Library()
my_library.library_manager()