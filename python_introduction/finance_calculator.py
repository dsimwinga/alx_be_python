#Declaring variables

#Getting monthly income from user
monthly_income = float(input("Enter your monthly income: "))

#Monthly total expenses
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

#Calculating Monthly savings
monthly_savings = monthly_income - total_monthly_expenses

#Yearly savings rate
annual_interest = 0.05

#Calculating the savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Displaying user monthly savings
print(f"Your monthly savings are ${monthly_savings}.")
#Displaying the projected annual savings with interest
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")