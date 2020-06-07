import math

annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your dream home:'))
monthly_salary = annual_salary / 12
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0

while current_savings < portion_down_payment * total_cost:
	months += 1
	current_savings += portion_saved * monthly_salary + (current_savings * r) / 12

print('Number of months:', months)