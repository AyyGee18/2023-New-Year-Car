class Vehicle:

    def __init__(self):
        self._maxspeed = None
        self._capacity = None

    def set_speed(self, speed):
        self._maxspeed = speed

    def get_speed(self):
        return self._maxspeed

    def set_capacity(self, cap):
        self._capacity = cap

    def get_capacity(self):
        return self._capacity

    def info(self):
        print("Max speed:", self._maxspeed, "\nCapacity:", self._capacity)


class Car(Vehicle):

    def __init__(self):

        super().__init__()
        self.__mark = None
        self.__model = None
        self.__body_type = None
        self.__year = None

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_bodytype(self, body):
        self.__body_type = body

    def get_bodytype(self):
        return self.__body_type

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def info(self):
        super().info()
        print("Mark:", self.__mark, "\nModel:", self.__model,
              "\nBody Type:", self.__body_type, "\nYear:", self.__year)


mercedes = Car()
mercedes.set_speed(250)
mercedes.set_capacity(2)
mercedes.set_bodytype("Coupe")
mercedes.set_year(2022)
mercedes.set_mark("Mercedes")
mercedes.set_model("CLA Coupe")
mercedes.info()
print("\n")

bmw = Car()
bmw.set_speed(240)
bmw.set_capacity(4)
bmw.set_bodytype("Coupe")
bmw.set_year(2022)
bmw.set_mark("BMW")
bmw.set_model("M8 Coupe")
bmw.info()
print("\n")

audi = Car()
audi.set_speed(240)
audi.set_capacity(4)
audi.set_bodytype("Coupe")
audi.set_year(2022)
audi.set_mark("BMW")
audi.set_model("M8 Coupe")
audi.info()
print("\n")

porsche = Car()
porsche.set_speed(280)
porsche.set_capacity(4)
porsche.set_bodytype("Sedan")
porsche.set_year(2022)
porsche.set_mark("Porsche")
porsche.set_model("Taycan")
porsche.info()
print("\n")
