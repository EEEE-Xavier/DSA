class Book():
    def __init__(self, isbn, title, category, publisher, year_Published, quantity):
        self.__isbn = isbn
        self.__title = title
        self.__category = category
        self.__publisher = publisher
        self.__yearPublished = year_Published
        self.__quantity = quantity

    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_category(self):
        return self.__category

    def get_publisher(self):
        return self.__publisher

    def get_yearPublished(self):
        return self.__yearPublished

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity
        return self.__quantity

    def __str__(self):
        return ("Books ISBN Number: {}\n"
                "Title: {}\n"
                "Category: {}\n"
                "Publisher: {}\n"
                "Year Published: {}\n"
                "Quantity: {}\n").format(self.get_isbn() ,self.get_title(), self.get_category(), self.get_publisher(), self.get_yearPublished(), self.get_quantity())




