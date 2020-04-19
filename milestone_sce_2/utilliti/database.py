
"""
concept with storing and retrieving books from a cvs file.
formet of the cvs file:


"""
books_file = "books.txt"

def create_book_table():
    with open(books_file, 'w'):
        pass

def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')
  #  books.append({'name': name, 'author':author, 'read': False})


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]  # [name,author,read], [name,author,read] etc

    return [ # [[name,author,read],[name,author,read]....]
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


    """
    data = [
    for line in files.readlines():
    value = line.strip().split(',')
    {'name': value[0], 'author': value[1], 'read': value[2]}
    ]
    return data
    
    with clause ko "contex manager " kahte hain
    """


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True

    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']}, {book['author']}, {book['read']} \n")



def delate_book(name):
    books = get_all_books()
    books = [book for book in books if book['name']!= name]
    _save_all_books()





  # global books
  #  books = [book for book in books if book['name']!= name]




