def test_product_init(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_property(product):
    assert product.price == 180000.0


def test_price_setter(product):
    if product.price <= 0:
        assert product.price == "Цена не должна быть нулевая или отрицательная"

def test_product_str(product):
    assert str(product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток 5 шт."

def test_product_add(product1, product2):
    assert product1 + product2 == 2580000.0
