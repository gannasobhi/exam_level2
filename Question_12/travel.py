from abc import ABC, abstractmethod


class Travel(ABC):
    @abstractmethod
    def calculate_total_cost(self):
        pass


    @abstractmethod
    def display_package_cost(self):
        pass