from src.base_product import BaseProduct
from src.print_mixin import PrintMixin

class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price


if __name__ == '__main__':
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

    product2 = Product.new_product("POCO", "256GB, Белый цвет, 50MP камера", 60000.0, 3)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    product2.price = 0
    # pragma: no cover
    print(product2.price)

    product2.price = 70000
    print(product2.price)
