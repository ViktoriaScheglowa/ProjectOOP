def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(first_category.products) == 3

    assert first_category.products_count == 4
    assert second_category.products_count == 4

    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_category_products_property(first_category):
    assert first_category.products == "[Product(name=Samsung Galaxy C23 Ultra, description=256GB, Серый цвет, 200MP камера, price=180000.0, quantity=5), Product(name=Iphone 15, description=512GB, Gray space, price=210000.0, quantity=8), Product(name=Xiaomi Redmi Note 11, description=1024GB, Синий, price=31000.0, quantity=14), Product(name=POCO, description=256GB, Белый цвет, 50MP камера, price=60000.0, quantity=3)]"


def test_category_products_setter(first_category, product):
    assert len(first_category.products_in_list) == 3
    first_category.products = product
    assert len(first_category.products_in_list) == 4
