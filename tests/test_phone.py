from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone 14", 120_000, 5, 0)

def test___repr__():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test___init__():
    assert phone1.name == 'iPhone 14' #создание экземпляра
    assert phone1.number_of_sim == 2 #количество симкарт > 0


