"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item
from src.phone import Phone

def test_Item_calculate_total_price():
    test_class = Item('Jho', 100.0, 10)
    test_data = test_class.calculate_total_price()
    assert test_data == 1000

def test_apply_discount():
    test_class = Item('Jho', 100.0, 10)
    test_data = test_class.apply_discount()
    assert test_data == None

def test_repr():
    item = Item("Электропельмень", 999999.99, 1)
    assert repr(item) == "Item('Электропельмень', 999999.99, 1)"

def test_str():
    item = Item("Электропельмень", 999999.99, 1)
    assert str(item) == "Электропельмень"


def test_add():
    item1 = Item("Электровеник", 1000, 1)
    phone1 = Phone("Кирпичфон", 3000, 10, 1)
    assert item1 + phone1 == 11
    assert phone1 + phone1 == 20
    assert item1 + 100 == None