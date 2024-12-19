class Book:
    def __init__(self, title, author, year):
        self.title = title      # Название книги
        self.author = author    # Автор книги
        self.year = year        # Год издания

    def get_info(self):
        # Возвращает информацию о книге в ( my_book )
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

my_book = Book("The Hunger Games", "Suzanne Collins", 2008)
print(my_book.get_info())