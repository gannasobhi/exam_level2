from vacation import Vacation


class Relaxation(Vacation):
    def __init__(self, spa_services , destination , price):
        super().__init__(destination , price)
        self.__spa_services = spa_services


    
    # Accessores    G,S
    def get_spa_services(self):
        return self.__spa_services
    

    # Extra methods
    def display_details(self):
        print('Destination: ', self.get_destination())
        print('Price: $'+ str( self.get_price()))
        print('Spa Services: ' + ','.join(self.__spa_services))