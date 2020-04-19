from utilliti import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete book
- 'q' to quit

your choice:   """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input!= 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


  # def prompt_delete_book() ask for b ook name and delete the book from list

def prompt_add_book():
    name = input("Enter the new book name  ")
    author = input("Enter the book author name  ")

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'yes' if book['read'] == '1' else 'no'
        print(f"{book['name']} by {book['author']}, read: {read}")

def prompt_read_book():
    name = input("Enter the book name whis you finished  ")

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of book you wish to delete  ")

    database.delate_book(name)

menu()
