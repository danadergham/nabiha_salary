salary = float(input("Please enter your salary for the month:"))
month=input("Enter the name of the month:")

savings_percentage= float(input("Please enter the percentage for savings: "))
rent_percentage= float(input("Please enter the percentage for rent: "))
electricity_percentage=float(input("Please enter the electricity percentage: "))

savings=(savings_percentage/100)*salary
rent=(rent_percentage/100)*salary
electricity=(electricity_percentage/100)*salary

total_expenses= savings+rent+electricity

remainder= salary - total_expenses

yearly_rent=rent*12
yearly_electricity= electricity*12

salary_squared= salary**2

import random
additional_savings=random.randint(10,100)
if savings>0:
    savings_division=additional_savings/savings
else:
    savings_division=0



left_after_savings=remainder+additional_savings


