from src.product import Product


class Category:
    name: str
    description: str
    products: list
    products_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.products_count += len(products)

    @property
    def add_product(self):
        new_product = ""
        for product in self.__products:
            new_product += f"{name}, {description}, {price}, {quantity}\n"
            return new_product

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.products_count += 1

    @property
    def products_in_list(self):
        return self.__products


    # def category_counters(self):
    #     cat_count = Category.category_count
    #     prods_count = Category.products_count


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                     "но и получение дополнительных функций для удобства жизни",
                        [product1, product2, product3])

    print(category.name)
    print(category.description)
    print(category.products)
    print(category.products_count)
    print(category.category_count)
