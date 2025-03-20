from src.product import Product


class Category:
    name: str
    description: str
    products_list: list
    products_count = 0
    category_count = 0

    def __init__(self, name, description, products_list):
        self.name = name
        self.description = description
        self.products_list = products_list
        Category.category_count += 1
        Category.products_count += len(products_list)


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                     "но и получение дополнительных функций для удобства жизни",
                        [product1, product2, product3])

    print(category.name)
    print(category.description)
    print(category.products_list)
    print(category.products_count)
    print(category.category_count)
