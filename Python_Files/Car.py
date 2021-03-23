class Car() :
    """Класс по созданию автомобиля"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        """Возвращаем описание автомобиля"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometr(self):
        """Пробег этого авто"""
        print("Пробег этого авто " + str(self.odometer_reading) + " км")

    def update_odometr(self, km):
        """Устанвливаем значение на одометре"""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Не стоит связываться")

    def increment_odometr(self, km):
        """Увеличиваем показания обометра на заданную величину"""
        self.odometer_reading += km

