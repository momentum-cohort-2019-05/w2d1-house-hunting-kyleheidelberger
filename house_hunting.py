
# gather inputs
annual_salary = int(input("What is your annual salary? $"))
portion_saved = int(input("What percent of your salary do you want to save? "))
total_cost = int(input("How much does your dream home cost? $"))
portion_down_payment = input("What percentage of the total cost do you want to put down? ")

if portion_down_payment == "":
    portion_down_payment = 25
else:
    portion_down_payment = int(portion_down_payment)

r = input("What percent is your annual rate of return on investments? ")
if r == "":
    r = 4
else:
    r = int(r)

# declare variables
current_savings = 0
portion_saved = portion_saved / 100
portion_down_payment = portion_down_payment / 100
r = r / 100
cost_down_payment = total_cost * portion_down_payment

# loop until savings meets down payment
number_months = 0
while current_savings <= cost_down_payment:
    monthly_savings = (annual_salary/12 * portion_saved) + current_savings*r/12
    current_savings = current_savings + monthly_savings
    number_months = number_months+1
print("You will have to save up for " + str(number_months) + " months.")
