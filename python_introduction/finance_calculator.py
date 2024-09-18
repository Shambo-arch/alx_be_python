monthly_income = int(input("Enter your monthly income  "))
total_monthly_expenses = int(input("Enter your total monthly expenses  "))
interest_rate = 0.05
time_in_year = 1
year_in_months = 12
monthly_savings = monthly_income - total_monthly_expenses
projected_savings = monthly_savings * year_in_months + monthly_savings * year_in_months * interest_rate
print("Projected Savings after", time_in_year, "with interest, is:", projected_savings)