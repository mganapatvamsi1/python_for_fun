from python_fun_code.Car import Car


class ElectricCar(Car):
      def __init__(self, number_of_wheels, seating_capacity, maximum_speed, brand, price):
          Car.__init__(self, number_of_wheels, seating_capacity, maximum_speed, brand, price)