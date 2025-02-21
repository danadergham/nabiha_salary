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

print("Salary for", month, ":", salary)
print("Savings (", savings_percentage, "%):", savings)
print("Rent (", rent_percentage, "%):", rent)
print("Electricity (", electricity_percentage, "%):", electricity)
print("Total expenses:", total_expenses)
print("Remaining after expenses:", remainder)
print("Estimated yearly rent:", yearly_rent)
print("Estimated yearly electricity:", yearly_electricity)
print("Salary squared (just for fun):", salary_squared)
print("Random additional savings:", additional_savings)
print("How many times the additional savings fit into savings:", savings_division)
print("Left salary after adding random savings:", left_after_savings)