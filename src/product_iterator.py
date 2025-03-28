from src.product import Product
from src.category import Category

class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("POCO", "256GB, Белый цвет, 50MP камера", 60000.0, 3)

    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                     "но и получение дополнительных функций для удобства жизни",
                        [product1, product2, product3,product4])

    iterator = ProductIterator(category)

    for product in iterator:
        print(product)