from python_fun_code.ElectricCar import ElectricCar
from python_fun_code.Car import Car

# ManiG = Person('Manikanta', 26.6)

first_car = Car(4, 5, 200, 'Mercedes E350', 65000)
print(first_car.number_of_wheels)
print(first_car.seating_capacity)
print(first_car.maximum_speed)
print(first_car.brand)
print(first_car.price)

electric_car_first = ElectricCar(1, 1, 111, 'neeon marioana', 300000)
print(electric_car_first.number_of_wheels)
print(electric_car_first.seating_capacity)
print(electric_car_first.maximum_speed)
print(electric_car_first.brand)
print(electric_car_first.price)
