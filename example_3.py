class Book:
    _id_counter = 1  # Класс-атрибут для хранения текущего значения уникального идентификатора

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls._id_counter
        cls._id_counter += 1
        return instance

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"

# Пример использования
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

print(book1)
print(book2)
print(book3)
