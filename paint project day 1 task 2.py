#sales tax project
square_feet = float(input("enter the number of square feet to be painted:"))
prize = float(input("enter the prize of the paint per gallon:"))
#The number of gallons of paint required
no_gallons= square_feet/115
print("The number of paint required is: ", no_gallons)
#The hours of labor required
hour_labor=(square_feet*8)/115
print("The hours of labor required is: ", hour_labor)
#The cost of the paint
cost = prize*no_gallons
print("The cost of paint is: ", cost)
#The labor charges
labor_charge = hour_labor*20
print("The labor charge is: ", labor_charge)
#Total cost of painting
total_cost = cost+labor_charge
print("The total cost of painting job is: ", total_cost)