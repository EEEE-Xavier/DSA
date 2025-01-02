from Book import Book
from RestockDetail import RestockDetail
def menu():
    print("BOOK MANAGEMENT SYSTEM")
    print("1. Add new Books")
    print("2. Display all Books")
    print("3. Sort books by Category using only Bubble Sort in ascending order.")
    print("4. Sort books by Publisher using Selection Sort in descending order")
    print("5. Sort books via Insertion Sort on Book Title (ascending)")
    print("6. Sort books via Merge Sort on Category(descending) follow by quantity (ascending)")
    print("7. Go to Restocking Menu")
    print("8. Set number of records per row to display")
    print("9. Populate Data")
    print("0. Exit Program")

def restock_menu():
    print("Restocking Menu:")
    print("1. Enter new stock arrival.")
    print("2. View Number of Stock in Stack.")
    print("3. Service top of Stack.")
    print("0. Return to Main Menu.")

def AddBook(bookList):
    new_isbn = input("Enter Book ISBN Number: ")
    new_title = input("Enter Book Title: ")
    new_category = input("Enter Book category: ")
    new_publisher = input("Enter publisher: ")
    new_yearPublished = input("Enter year published: ")


    add = Book(new_isbn, new_title, new_category, new_publisher, new_yearPublished, quantity=0)
    bookList.append(add)

    print("New Book added successfully!")
    print()
    return bookList


def bubble(bookList):
    count = 0
    n = len(bookList)
    for a in range(n-1):
        swapped = False
        count += 1
        for b in range(0, n-1):
            if bookList[b].get_category() > bookList[b+1].get_category():
                tmp = bookList[b]
                bookList[b] = bookList[b+1]
                bookList[b+1] = tmp

                swapped = True
        print()
        print(f"Pass: {count}")
        print("-------------------------------")
        for book in bookList:
            print(f"ISBN number:", book.get_isbn())
        print("-------------------------------")
        print()

        if swapped == False:
            break

def selection(bookList):
    n = len(bookList)
    count = 0
    for a in range(n-1):
        max = a
        count += 1
        print("----------------------")

        for b in range(a + 1, n):
            if bookList[b].get_publisher() > bookList[max].get_publisher():
                max = b

        temp = bookList[a]
        bookList[a] = bookList[max]
        bookList[max] = temp
        a += 1
        print(f"Pass: {count}")
        for books in bookList:
            print("ISBN number: ", books.get_isbn())
        print()
    return bookList

def insertionSort(bookList):
    Pass = 0
    n = len(bookList)
    for i in range(1, n):
        currentBook = bookList[i]
        value = currentBook.get_title()
        pos = i
        while pos > 0 and value < bookList[pos-1].get_title():
            bookList[pos] = bookList[pos-1]
            pos -= 1
        bookList[pos] = currentBook
        Pass += 1
        print("Pass:", Pass)
        for books in bookList:
            print("ISBN number: ", books.get_isbn())
        print()
    return bookList

def mergeSort(bookList):
    if len(bookList) <= 1:
        return bookList
    else:
        mid = len(bookList)//2
        left = mergeSort(bookList[:mid])
        right = mergeSort(bookList[mid:])
        newList = mergeSortedLists(left, right)
        for i in range(len(newList)):
            bookList[i] = newList[i]
    return bookList

def mergeSortedLists(listA, listB):
    newList = []
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a].get_category() > listB[b].get_category():
            newList.append(listA[a])
            a += 1
        elif listA[a].get_category() < listB[b].get_category():
            newList.append(listB[b])
            b += 1
        else:
            if listA[a].get_quantity() < listB[b].get_quantity():
                newList.append(listA[a])
                a += 1
            else:
                newList.append(listB[b])
                b += 1

    while a < len(listA):
        newList.append(listA[a])
        a += 1

    while b < len(listB):
        newList.append(listB[b])
        b += 1

    print("New List:")
    for books in newList:
        print("ISBN number: ", books.get_isbn())
    print()

    return newList

def sequentialSearch(bookList, target):
    n  = len(bookList)
    for i in range(n):
        if bookList[i].get_isbn() == target:
            return True

    return False


def AddNewStock(bookList, stack):
    while True:
        target = input("Enter book ISBN: ")
        if sequentialSearch(bookList, target):
            qty = int(input("Enter qty to restock: "))
            RD = RestockDetail(target, qty)
            stack.push(RD)
            print("Delivery arrival added successfully")
            break
        else:
            print("Book Not Found. Please try again!")


def LengthStack(stack):
    if stack.isEmpty():
        print()
        print("Number of Delivery in Stack:", 0)
        print()
    else:
        print()
        print("Number of Delivery in Stack:", len(stack))
        print()

def ConfirmDelivery(bookList, stack):
    if not stack.isEmpty():
        delivery = stack.pop()
        print(f"Delivery ISBN: {delivery.get_isbn()}")
        for book in bookList:
            if book.get_isbn() == delivery.get_isbn():
                print()
                print("Display Pending Stock Arrival")
                print("-----------------------------")
                print(book)
                print("-----------------------------")
                print(f"New Stock: {delivery.get_quantity()}")
                print("-----------------------------")
                print()
                print(f"Remaining restock in stock: {len(stack)}")
                print()
                confirm = input("Proceed with restocking (Y/N): ")
                if confirm.upper() == "Y":
                    updated = book.get_quantity() + delivery.get_quantity()
                    book.set_quantity(updated)
                    print(f"Book ISBN : {book.get_isbn()} updated stock: {updated}")
                    return bookList
                elif confirm.upper() == "N":
                    stack.push(delivery)
                    print(f"Product {book.get_isbn()} returned to stack!")
                else:
                    print("Invalid input")

    else:
        print()
        print("No deliveries to handle.")
        print()

def DisplayRecursive(bookList, row_num = 1):
    if len(bookList) == 0:
        return
    else:
        column_width = 45
        display = bookList[:row_num]
        remaining = bookList[row_num:]

        #Label are the Strings such as "ISBN: "
        #Getter are the bookList: bookList.get_isbn()
        fields = [
            ("ISBN: ", lambda bookList: bookList.get_isbn()),
            ("Title: ", lambda bookList: bookList.get_title()),
            ("Category: ", lambda bookList: bookList.get_category()),
            ("Publisher: ", lambda bookList: bookList.get_publisher()),
            ("Year Published: ", lambda bookList: bookList.get_yearPublished()),
            ("Quantity: ", lambda bookList: bookList.get_quantity())
        ]

        for label, getter in fields:
            for book in display:
                print(f"{label}{getter(book):<{column_width - len(label)}}", end="")
            print()

        print()
        DisplayRecursive(remaining, row_num)

