import pytest


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(first_category.products) == 3

    assert first_category.products_count == 4
    assert second_category.products_count == 4

    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_category_products_property(first_category):
    expected_output = "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток 5 шт.\nIphone 15, 210000.0 руб. Остаток 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток 14 шт.".strip()
    actual_output = "\n".join(str(product) for product in first_category.products).strip()
    assert expected_output == actual_output


def test_category_products_setter(first_category, product):
    assert len(first_category.products_in_list) == 3
    first_category.products = product
    assert len(first_category.products_in_list) == 4


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 14 шт."


def test_product_iterator(product_iterator):
    assert product_iterator.index == 0
    assert next(product_iterator).name == "55\" QLED 4K"
    with pytest.raises(StopIteration):
        next(product_iterator)
    assert product_iterator.index == 1
