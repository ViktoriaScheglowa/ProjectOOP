from src.product import Product


class Order():
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.product_cost = self.__price* self.quantity

    def __repr__(self):
        return f"куплен {self.name}. колличество {self.quantity}. Итоговая стоимость {self.product_cost}."

# допустим вот товар
coca_cola = Product('Кока Кола', 'Та самая легендарная', 125, 100)

# создаём заказ
my_order = Order(name=coca_cola,quantity=5)

print(my_order.product_cost)  # 625
print(repr(my_order)) # куплен Кока Кола. колличество 5. Итоговая стоимость 625