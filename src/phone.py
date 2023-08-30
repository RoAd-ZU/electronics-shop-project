# -*- coding: utf-8 -*-
from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name_}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name_