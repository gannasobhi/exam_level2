from hr_department import HR
from technical_department import Technical


tech_dept = Technical('Tech')
hr_dept = HR('HR')

tech_dept.add_employee('Alice')
tech_dept.add_employee('Bob')
hr_dept.add_employee('Charlie')

print(tech_dept.display_department())
print(hr_dept.display_department())