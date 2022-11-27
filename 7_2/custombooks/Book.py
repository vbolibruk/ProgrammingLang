from abc import ABC, abstractmethod

class CabinRental:
    """
    Абстрактний клас Book 
    Розробник: Влад
    Версія: 1.0

    Поля:
    title - Назва книжки
    price - Ціна
    """

class Book(ABC):
    
    def __init__(self, title = "", price= 0.0):
        """
        Ініціалізація об'єкта типу Book
        """

        self.__title =  title
        self.__price =  price

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    @abstractmethod
    def setPrice(self):
        """
        Абстрактний метод установки ціни
        """
        pass

