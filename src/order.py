from src.product import Product


class Order(Product):
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.product_cost = self.__price* self.quantity

    def __repr__(self):
        return f"куплен {self.name}. колличество {self.quantity}. Итоговая стоимость {self.product_cost}."