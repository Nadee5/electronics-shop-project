"""Здесь надо написать тесты с использованием pytest для модуля item"""

import os
import csv
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
Item.pay_rate = 0.8

def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000

def test_name():
    item = Item('Телефон', 10000, 5)
    assert item.name == 'Телефон'
    item.name = 'Phone'
    assert item.name == 'Phone'
    item.name = 'SuperSUPhone'
    assert item.name == 'SuperSUPho'


def test_instantiate_from_csv():
    path_file = 'src/test_items.csv'
    head, tail = os.path.split(path_file)
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_FOR_PATH = os.path.join(CURRENT_DIR, tail)
    test_list = []
    with open(DATA_FOR_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_item = Item(row['name'], row['price'], row['quantity'])
            test_list.append(new_item)
    assert test_list[4].name == 'Клавиатура'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
