from src.phone import Phone
def test_repr():
    phone = Phone("Кирпичфон", 3000, 10, 1)
    assert repr(phone) == "Phone('Кирпичфон', 3000, 10, 1)"

def test_str():
    phone = Phone("Кирпичфон", 3000, 10, 1)
    assert str(phone) == 'Кирпичфон'

