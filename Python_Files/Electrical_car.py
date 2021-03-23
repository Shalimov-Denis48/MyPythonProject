from Car import Car

class Battery():
    """Простая модель аккумулятора для электромобиля"""

    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        """Выводит информацию о мощности батареи"""
        print("Этот автомобиль имеет батарею мощностью " + str(self.battery) + " киловат")

class ElectricCar(Car) :
    """Аспекты для электромобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов класса родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_name(self):
        """Переопределение родительского метода"""
        desc = str(self.year) + ' ' + self.model
        return desc.title()