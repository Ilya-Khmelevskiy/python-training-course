from car import Car
from battery import Battery


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        self.battery.describe_battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank.")
