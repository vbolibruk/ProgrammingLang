# Розробити клас CabinRental:
# - ціле значення номера кімнати
# - дійсне значення тижневої вартості аренди кімнати
# - методи-геттери для значень полів
# - конструктор має отримувати ціле число - номер кімнати
# - вартість аренди: 950 для кімнат 1, 2, 3
#   інші кімнати - 1100

# Розробити клас-нащадок HolidayCabinRental
# - конструктор отримує номер та додає 150 до аренди

# Розробити демо програму DemoCabinRental
# - створюється об'єкт кожного класу
# - демонстрація усіх методів

# Кожен клас повинен бути збереженим у окремому файлі

class CabinRental:

    def __init__(self,cabinNumber):
        self.__cabinNumber = cabinNumber
        if (cabinNumber >= 1) and (cabinNumber <= 3):
            self.__rentalRate = 950
        else:
            self.__rentalRate = 1100

    @property
    def cabinNumber(self):
        return self.__cabinNumber

    @property
    def rentalRate(self):
        return self.__rentalRate

    def printInfo(self):
        print(f'Cabin number: {self.__cabinNumber}'
              f'\nRental rate: {self.__rentalRate}')

class HolidayCabinRental(CabinRental):

    def __init__(self,cabinNumber):
        super().__init__(cabinNumber)
        self.__rentalRate = super().rentalRate + 150

    def printInfo(self):
        print(f'Cabin number: {self.cabinNumber}'
              f'\nHoliday rental rate: {self.__rentalRate}')

c1 = CabinRental(3)
c2 = CabinRental(10)

c1.printInfo()
c2.printInfo()

print(f"Rental rate in c2 is {c2.rentalRate}")

c3 = HolidayCabinRental(3)
c4 = HolidayCabinRental(10)

print("")
c3.printInfo()
c4.printInfo()

print(f"Holiday rental rate in c4 is {c4.rentalRate}")

# ПРОБЛЕМА!
# Завдання. Подумайте і модифікуйте клас HolidayCabinRental,
# щоб вивід поточної програми повністю був аналогічний виводу
# програми DemoCabinRental.java.
# Підказка. Пошукайте, яким чином можна створювати поля, що
# є аналогами полів protected мови java.
