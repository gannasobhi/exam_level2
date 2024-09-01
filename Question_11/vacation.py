from abc import ABC, abstractmethod


class Vacation(ABC):
    def __init__(self,destination,price):
        self.__destination = destination
        self.__price = price

    
    # Accessores   G,S
    def get_destination(self):
        return self.__destination
    
    def get_price(self):
        return self.__price
    

    # Extra methods
    @abstractmethod
    def display_details(self):
        pass