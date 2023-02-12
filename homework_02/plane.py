"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    # cargo = 0
    # max_cargo = 2500

    def __init__(self,
                 weight,
                 fuel,
                 fuel_consumption,
                 max_cargo: int = 2500,
                 cargo: int = 0):
        super().__init__(
                         # self,
                         weight=weight,
                         fuel=fuel,
                         fuel_consumption=fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, ext_cargo):
        sum_cargo = self.cargo + ext_cargo
        if sum_cargo <= self.max_cargo:
            self.cargo = sum_cargo
            return self.cargo
        else:
            raise CargoOverload('Перегруз')

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result


