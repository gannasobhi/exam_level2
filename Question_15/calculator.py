class Calculator:
    def __init__(self,model_name , color ,length , width):
        self.__model_name = model_name
        self.__color = color
        self.__length = length 
        self.__width = width 


    
    # Accessores  G,S
    def get_model_name(self):
        return self.__model_name
    
    def get_color(self):
        return self.__color
    
    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width
    

    # Extra methods
    @staticmethod
    def add_numbers(a,b):
        return a+b
    
    @staticmethod
    def subtract_numbers(a,b):
        return a-b
    
    @staticmethod 
    def multiply_numbers(a,b):
        return a*b
    
    @staticmethod
    def divide_numbers(a,b):
        return a/b