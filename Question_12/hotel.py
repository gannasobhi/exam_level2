from travel import Travel


class Hotel(Travel):
    def __init__(self,nights,cost_per_night):
        self.__nights = nights
        self.__cost_per_night = cost_per_night


    
    # Accessores   G,S
    def get_nights(self):
        return self.__nights
    
    def get_cost_per_night(self):
        return self.__cost_per_night
    

    # Extra meyhods
    def calculate_total_cost(self):
        return self.__nights * self.__cost_per_night


    def display_package_cost(self):
        print('Total Cost for Hotel Package:', self.calculate_total_cost())