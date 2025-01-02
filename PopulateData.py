import Book

def populateData():
    bookList = []
    newBook = Book.Book("B102", "The don't laugh challenge", "Humor", "Oreilly", 2019, 2000)
    bookList.append(newBook)
    newBook = Book.Book("B107", "How to draw everything for kids", "Kids Art", "Wiley", 1998, 320)
    bookList.append(newBook)
    newBook = Book.Book("B101", "Book on Planet Earth", "Science", "Oreilly", 2021, 150)
    bookList.append(newBook)
    newBook = Book.Book("B105", "Kids Encyclopedia", "Encyclopedia", "Ladybird", 1999, 350)
    bookList.append(newBook)
    newBook = Book.Book("B104", "I am 10 and amazing", "Inspiration", "Wiley", 2022, 1500)
    bookList.append(newBook)
    newBook = Book.Book("B106", "Ocean Animals", "Science", "Oreilly", 2023, 50)
    bookList.append(newBook)
    newBook = Book.Book("B103", "Inspiring Stories for Kids", "Inspiration", "Oreilly", 2022, 500)
    bookList.append(newBook)
    print("Books populated!\n")
    return bookList
