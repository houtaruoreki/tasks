class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_production_year(self):
        return self.__production_year

    def get_color(self):
        return self.__color

    def get_horse_power(self):
        return self.__horse_power
    
    def is_sport_car(self):
        return self.__is_sport_car
    
    def change_color(self, new_color):
        if self.__color != new_color:
            self.__color = new_color
            return True
        else: return False

    def increase_horse_power(self, hp):
        if hp>0:
            self.__horse_power += hp
            return True
        else: return False