# import Car импортирование всего модуля
from Car import *
from Electrical_car import ElectricCar

a4 = Car('audi', 'a4', 2018)
print(a4.description_name())

tesla = ElectricCar('tesls', 's', 2016)
tesla.battery.description_battery()