class Car:

    def __init__(self,y,m, speed):
        self.__year_model = y
        self.__make = m
        self.__speed = speed

    def calc_accelerate(self):
        self.__speed += 5

    def calc_brake(self):
        self.__speed -= 5
        if self.__speed == 0:
            self.__speed = 0

    def get_year(self):
        return self.__year

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    
         
    