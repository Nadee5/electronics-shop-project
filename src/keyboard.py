from src.item import Item


class MixinLang:

    __language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language

class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    def __str__(self):
        return f"{self.name}"
