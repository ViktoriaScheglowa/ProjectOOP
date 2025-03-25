class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"

    def __repr__(self):
        return self.__str__()

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
    print(product2.price)

    product2.price = 70000
    print(product2.price)
