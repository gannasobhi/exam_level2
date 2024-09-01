from vacation import Vacation


class Adventure(Vacation):
    def __init__(self,sea_activites, destination, price):
        super().__init__(destination,price)
        self.__sea_activites = sea_activites


    # Accessores    G,S
    def get_sea_activites(self):
        return self.__sea_activites
    


    # Extra methods
    def display_details(self):
        print('Destination: ', self.get_destination())
        print('Price: $'+ str(self.get_price()) ) 
        print('Sea Activites: ' + ','.join((self.__sea_activites)))