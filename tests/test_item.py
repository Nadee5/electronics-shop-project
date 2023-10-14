"""Здесь надо написать тесты с использованием pytest для модуля item"""

import os
import csv
from src.item import Item
from src.phone import Phone

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
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test___repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test___str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'

def test___add__():
    item_1 = Item("Смартфон", 10000, 20)
    phone_1 = Phone("iPhone 14", 120_000, 5, 2)
    item_2 = 10
    assert item_1 + phone_1 == 25
    assert phone_1 + phone_1 == 10
    assert item_1 + item_2 == 'Сложение невозможно'
    assert phone_1 + item_2 == 'Сложение невозможно'


