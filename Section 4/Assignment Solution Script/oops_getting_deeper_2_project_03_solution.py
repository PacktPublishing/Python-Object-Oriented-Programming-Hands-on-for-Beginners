# Project 1

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, make, model, edition, color, average_mileage, gas_tank_capacity,
                 moon_roof=False):
        self.make = make
        self.model = model
        self.edition = edition
        self.color = color
        self.average_mileage = average_mileage
        self.gas_tank_capacity = gas_tank_capacity
        self.moon_roof = moon_roof
        self.engine_status = "Not Running"
        self.speed = 0

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def increase_speed_by(self, increase_by):
        pass

    @abstractmethod
    def decrease_speed_by(self, decrease_by):
        pass


class Audi(Car):
    __max_speed_in_miles = 0
    __name = ""

    def __init__(self, model, edition, color, average_mileage, gas_tank_capacity,
                 moon_roof=False):
        self.__make = "Audi"
        super().__init__(self.__make, model, edition, color, average_mileage, gas_tank_capacity,
                         moon_roof)

    @property
    def max_speed_in_miles(self):
        return self.__max_speed_in_miles

    @max_speed_in_miles.setter
    def max_speed_in_miles(self, value):
        if 120 <= value <= 220:
            self.__max_speed_in_miles = value
        else:
            print("Maximum speed must be between 120 and 220k!")
            exit(500)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def start(self):
        if self.engine_status == "Running":
            print("{} {} : {}".format(self.__make, self.model, "You already started it!"))
        else:
            self.engine_status = "Running"
            print("{} {} : {}".format(self.__make, self.model, self.engine_status))

    def stop(self):
        if self.engine_status == "Not Running":
            print("{} {} : {}".format(self.__make, self.model, "Engine is not running!"))
        else:
            self.engine_status = "Not Running"
            print("{} {} : {}".format(self.__make, self.model, "Stopped the engine!"))

    def increase_speed_by(self, increase_by):
        if self.engine_status == "Running":
            if self.max_speed_in_miles - self.speed >= increase_by:
                self.speed += increase_by
                print("{} {} : {} {}".format(self.__make, self.model, "Increasing the speed to", self.speed))
            else:
                print("{} {} : {} {}, {} {}, {} {}".format(self.__make, self.model,
                                                           "Requested", increase_by,
                                                           "Current Speed", self.speed,
                                                           "Max Speed", self.max_speed_in_miles))
        else:
            print("{} {} : {}".format(self.__make, self.model, "Please start the engine first!"))

    def decrease_speed_by(self, decrease_by):
        if self.engine_status == "Running":
            if self.speed - decrease_by >= 0:
                self.speed -= decrease_by
                print("{} {} : {} {}".format(self.__make, self.model, "Decreasing the speed to", self.speed))
            else:
                print("{} {} : {} {}, {} {}".format(self.__make, self.model,
                                                    "Req. to decrease speed by", decrease_by,
                                                    "Current Speed", self.speed))
        else:
            print("{} {} : {}".format(self.__make, self.model, "Please start the engine first!"))

    def __str__(self):
        return "{} {} : {}".format(self.__make, self.model, self.__name)


def main():
    car1 = Audi("A8", "2020", "Black", "20.00", "10G", True)
    car1.max_speed_in_miles = 200
    car1.name = "Audi-100"
    print(car1.__str__())
    car1.start()
    car1.decrease_speed_by(10)
    car1.increase_speed_by(50)
    car1.increase_speed_by(30)
    car1.decrease_speed_by(10)
    car1.decrease_speed_by(10)
    car1.stop()


if __name__ == '__main__':
    main()
