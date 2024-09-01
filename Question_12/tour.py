from travel import Travel


class Tour(Travel):
    def __init__(self,days,cost_per_day):
        self.__days = days
        self.__cost_per_day = cost_per_day


    # Accessores  G,S
    def get_days(self):
        return self.__days
    
    def get_cost_per_day(self):
        return self.__cost_per_day
    

    # Extra methods
    def calculate_total_cost(self):
        return self.__days * self.__cost_per_day * 0.9
    
    def display_package_cost(self):
        print('Total Cost for Tour package After 10% discount: ', self.calculate_total_cost())