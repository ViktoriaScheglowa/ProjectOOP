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

    def __str__(self):
        return f'{self.name}, количество продуктов: {Category.products_count} шт.'

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.products_count += 1
        else:
            raise TypeError

    def product_new(self):
        new_product = ""
        for product in self.__products:
            new_product += f"{product.name}, {product.description}, {product.price} руб. Остаток: {product.quantity}шт.\n"
            return new_product

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.products_count += 1

    @property
    def products_in_list(self):
        return self.__products


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                     "но и получение дополнительных функций для удобства жизни",
                        [product1, product2, product3])

    print(category.name)
    print(category.description)

    print(category.products_count)
    print(category.category_count)

    product4 = Product("POCO", "256GB, Белый цвет, 50MP камера", 60000.0, 3)
    category.products = product4
    print(category.products)
