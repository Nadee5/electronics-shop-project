import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        Добавление экземпляра в список all.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        """Возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Записывает название товара согласно условиям."""
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            sale_name = list(new_name)[:10]
            self.__name = ''.join(sale_name)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path_file):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла.csv.
        """
        Item.all.clear()
        head, tail = os.path.split(path_file)
        CURRENT_DIR = os.path.dirname(__file__)
        DATA_FOR_PATH = os.path.join(CURRENT_DIR, tail)
        with open(DATA_FOR_PATH, encoding='cp1251', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string):
        """
        Cтатический метод, возвращающий число из числа-строки.
        """
        return int(float(string))
