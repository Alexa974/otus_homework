from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # weight = 1000
    # started = False
    # fuel = 20
    # fuel_consumption = 5.0

    def __init__(self,
                 weight: int = 1000,
                 fuel: int = 20,
                 fuel_consumption: float = 5.0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def move(self, distance):
        if self.fuel_consumption * distance <= self.fuel:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel('Не достаточно топлива для преодоления дистанции')

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Не достаточно топлива для запуска')
