# -*- coding: utf-8 -*-
# from src.phone import Phone
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    @property
    def name_(self):
        return self.__name

    @name_.setter
    def name_(self, name_1):
        if len(name_1) > 10:
            self.__name = name_1[:10]
        else:
            self.__name = name_1

    @classmethod
    def instantiate_from_csv(cls, csvfile):
        with open(csvfile, newline='') as new_:
            new_datas = csv.DictReader(new_)
            for row in new_datas:

                # print(cls(datas['name'], datas['price'], datas['quantity']))
                data = cls(row['name'], row['price'], row['quantity'])
                cls.all.append(data)


    @staticmethod
    def string_to_number(num):
        return int(float(num))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        multiply = self.price * self.quantity
        return multiply

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name


    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            return None



