class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __setattr__(self, name, value):
        if name == 'name':
            if not value[0].isupper() or not value.isalpha():
                raise ValueError("Имя должно начинаться с заглавной буквы и содержать только буквы")
        elif name == 'age':
            if not isinstance(value, int) or not (0 <= value <= 120):
                raise ValueError("Возраст должен быть целым числом от 0 до 120")
        elif name == 'email':
            if '@' not in value:
                raise ValueError("Email должен содержать символ @")

        super().__setattr__(name, value)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, email={self.email})"

# Пример использования
try:
    person = Person("Иван", 30, "ivan@example.com")
    print(person)
except ValueError as e:
    print(e)

try:
    person = Person("иван", 30, "ivan@example.com")
    print(person)
except ValueError as e:
    print(e)

try:
    person = Person("Иван", 130, "ivan@example.com")
    print(person)
except ValueError as e:
    print(e)

try:
    person = Person("Иван", 30, "ivanexample.com")
    print(person)
except ValueError as e:
    print(e)
