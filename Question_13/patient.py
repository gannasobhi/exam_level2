from person import Person


class Patient(Person):
    def __init__(self,medical_history, name , age):
        super().__init__(name , age)
        self.__medical_history = medical_history


    
    # Accessores  G,S
    def get_medical_history(self):
        return self.__medical_history
    

    # Extra methods
    def get_details(self):
      return  print('Patient Name:',self.get_name(),' Age:',self.get_age(),'  Medical History:',self.__medical_history)