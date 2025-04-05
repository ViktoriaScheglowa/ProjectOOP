from src.product import Product


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


if __name__ == '__main__':
    lawngrass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    lawngrass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(lawngrass1.name)
    print(lawngrass1.description)
    print(lawngrass1.price)
    print(lawngrass1.quantity)

    print(lawngrass1.country)
    print(lawngrass1.germination_period)
    print(lawngrass1.color)

    lawngrass_sum = lawngrass1 + lawngrass2
    print(lawngrass_sum)