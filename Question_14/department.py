class Department:
    def __init__(self,dept_name):
        self.__dept_name = dept_name
        self.__emps_list = []

    

    # Accessores  G,S
    def get_dept_name(self):
        return self.__dept_name
    

    

    # Extra methods
    def add_employee(self,emp_name):
        self.__emps_list.append(emp_name)


    def display_department(self):
        print('Department:',self.__dept_name +'  Employess: '+ ','.join(self.__emps_list ))