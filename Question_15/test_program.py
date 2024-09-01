from calculator import Calculator


samsung_calculator = Calculator(model_name='samsung' , color='grey', length=10 ,width=2) 

print('Add Numbers = ', Calculator.add_numbers(10,2))
print('Subtract Numbers = ' , Calculator.subtract_numbers(10,2))
print('Multiply Numbers = ', Calculator.multiply_numbers(10,2))
print('Divide Numbers = ' , Calculator.divide_numbers(10,2))