def test_product_init(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_property(product):
    assert product.price == 180000.0


def test_price_setter(product):
    if price <= 0:
        assert price == "Цена не должна быть нулевая или отрицательная"
