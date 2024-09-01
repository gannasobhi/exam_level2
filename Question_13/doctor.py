from person import Person


class Doctor(Person):
    def __init__(self,specialty, name, age):
        super().__init__(name, age)
        self.__specialty = specialty

    
    # Accessores  G,S
    def get_specialty(self):
        return self.__specialty
    

    # Extra methods
    def get_details(self):
      print( 'Doctor Name:' , self.get_name() , ' Age:' ,self.get_age() , ' Specialty: ',self.__specialty)