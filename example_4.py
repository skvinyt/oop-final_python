class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __setattr__(self, name, value):
        if name == 'price':
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("Цена должна быть положительным числом")
        elif name == 'quantity':
            if not isinstance(value, int) or value < 0:
                raise ValueError("Количество должно быть неотрицательным целым числом")

        super().__setattr__(name, value)

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

# Пример использования
try:
    product1 = Product("Laptop", 29995.99, 10)
    print(product1)
except ValueError as e:
    print(e)

try:
    product2 = Product("Smartphone", -500, 5)
    print(product2)
except ValueError as e:
    print(e)

try:
    product3 = Product("Tablet", 300, -3)
    print(product3)
except ValueError as e:
    print(e)

try:
    product4 = Product("Headphones", 5059, 20)
    print(product4)
except ValueError as e:
    print(e)
