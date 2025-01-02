class RestockDetail():
    def __init__(self, isbn, quantity):
        self.__isbn = isbn
        self.__quantity = quantity

    def get_isbn(self):
        return self.__isbn

    def get_quantity(self):
        return self.__quantity

    def set_isbn(self, isbn):
        self.__isbn = isbn
        return self.__isbn
    def set_quantity(self, quantity):
        self.__quantity = quantity
        return self.__quantity