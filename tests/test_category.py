def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(first_category.products_list) == 3

#def test_category_counters():
    # запоминаем сколько было
    #cat_count = Category.category_count
    #prods_count = Category.products_count

    # меняет значения счётчиков
    #new_prod = Product('a', 'b', 1, 2)
    #new_cat = Category('a', 'b', [new_prod])

    # проверяем, что счетчики изменились именно так, как должны были
    #assert Category.category_count = cat_count + 1
    #assert Category.products_count = prods_count + 1

    assert first_category.products_count == 4
    assert second_category.products_count == 4

    #assert first_category.category_count == 2
    #assert second_category.category_count == 2
