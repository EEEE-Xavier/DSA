from PopulateData import populateData
from functions import AddBook, bubble, selection, insertionSort, mergeSort, menu, restock_menu, AddNewStock, LengthStack, ConfirmDelivery, DisplayRecursive
from StockStack import StockStack
row_num = 1
stack = StockStack()
def main():
    global row_num
    bookList = []
    while True:

        menu()
        user_input = int(input("Please select: "))
        print()
        if user_input == 0:
            print("Good bye!")
            break

        elif user_input == 1:
            AddBook(bookList)


        elif user_input == 2:
            if bookList != []:
                print("Book List:")
                print("-------------------------")
                DisplayRecursive(bookList, row_num)
            else:
                print("There are currently no books in the system!")
                print()

        elif user_input == 3:
            bubble(bookList)
            print("Book List:")
            print("-------------------------")
            DisplayRecursive(bookList, row_num)

        elif user_input == 4:
            selection(bookList)
            print("Book List:")
            print("-------------------------")
            DisplayRecursive(bookList, row_num)

        elif user_input == 5:
            insertionSort(bookList)
            print("Book List:")
            print("-------------------------")
            DisplayRecursive(bookList, row_num)

        elif user_input == 6:
            mergeSort(bookList)
            print("Book List:")
            print("-------------------------")
            DisplayRecursive(bookList, row_num)

        elif user_input == 7:
            global stack
            while True:
                restock_menu()
                restock_input = int(input("Please Select: "))
                if restock_input == 0:
                    print()
                    break
                elif restock_input == 1:
                    print()
                    AddNewStock(bookList, stack)
                    print()
                elif restock_input == 2:
                    print()
                    LengthStack(stack)
                    print()
                elif restock_input == 3:
                    print()
                    ConfirmDelivery(bookList, stack)
                    print()



        elif user_input == 8:
            row_num = int(input("Please enter the number of records to display per row: "))
            print(f"Display rows set to {row_num}")
            print()

        elif user_input == 9:
            bookList = populateData()


if __name__ == "__main__":
    main()




