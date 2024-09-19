
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
  author = Author.objects.get(name=author_name)
  books = Book.objects.filter(author=author)
  for book in books:
    print(f"Book: {book.title}")

# List all books in a library
def get_books_in_library(library_name):
  library = Library.objects.get(name=library_name)
  books = library.books.all()
  for book in books:
    print(f"Book: {book.title}")

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    Librarian.objects.get(library=)
 
