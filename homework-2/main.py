from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 6  # ОТРЕДАКТИРОВАНО ЗНАЧЕНИЕ!!! (5) в файле 5 записей с данными по товарам
    #ВАЖНО!!! Item[0] был создан вручную (main, строка 4), инициализирован и добавлен в класс (задание первой части)
    # +дописаны 5 строк из файла, итого 6
    # если не так, то я не понимаю, что происходит -.-

    item1 = Item.all[0]
    assert item1.name == 'СуперСмарт' # ОТРЕДАКТИРОВАНО ЗНАЧЕНИЕ!!! ('Смартфон')
    # ВАЖНО!!! в условии README "В противном случае, обрезать строку (оставить первые 10 символов)"
    # => имя было перезаписано на СуперСмарт, разве не так?

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
