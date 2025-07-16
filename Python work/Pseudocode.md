Task 1
Create a flowchart and pseudocode for these cases:
Define if a given number is prime or not.
A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. 
Or, it is a natural number that can be divided only by 1 and itself.

# Task 1: Prime Number Check

# Pseudocode:
# 1. Start
# 2. Input number
# 3. If number <= 1: Not Prime
# 4. For i from 2 to sqrt(number):
#      If number % i == 0: Not Prime
# 5. If no divisors found: Prime
# 6. End

# Flowchart Steps:
# [Start] -> [Input Number] -> [Is number <= 1?]
#   Yes -> [Not Prime] -> [End]
#   No -> [i = 2 to sqrt(n): Is n % i == 0?]
#     Yes -> [Not Prime] -> [End]
#     No -> [Prime] -> [End]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print("The number is Prime.")
else:
    print("The number is Not Prime.")

Task 2
French tax deduction
Rule 1: Income Threshold Based on Tax Reference Income (RFR)
To qualify for certain tax reductions or exemptions, the taxpayer's tax reference income (revenu fiscal de référence) must fall below specific annual limits set by the French government.
Rule 2: Family Quotient Advantage
Taxpayers receive reductions based on their family situation, through the “quotient familial” system.
The more dependents (children, elderly relatives, etc.), the more parts are counted in your household, which reduces taxable income.
There is a limit to the tax reduction per half-share, which was €1,759 in 2024.
Rule 3: Eligibility Through Deductible Expenses and Credits
Certain life expenses can make taxpayers eligible for tax reductions or credits, such as:
Home help services (e.g., cleaners, nannies): 50% credit on eligible costs
Childcare for children under 6: 50% credit on up to €3,500 of expenses
Energy-saving home improvements: Eligible for the “MaPrimeRénov” or other eco-tax benefits


# Task 2: French Tax Deduction Calculator

def calculate_tax_deductions(income, num_half_shares, childcare_expense, home_help_expense, renovation_eligible):
    # Rule 1: Income Threshold
    income_threshold = 27000  # Example threshold; real value may vary
    income_status = "Eligible" if income <= income_threshold else "Not eligible"

    # Rule 2: Family Quotient
    max_reduction_per_half_share = 1759
    family_quotient_reduction = num_half_shares * max_reduction_per_half_share

    # Rule 3: Deductible Expenses
    childcare_credit = min(childcare_expense, 3500) * 0.5
    home_help_credit = home_help_expense * 0.5
    renovation_credit = 1500 if renovation_eligible else 0  # Sample fixed credit

    total_credits = childcare_credit + home_help_credit + renovation_credit

    return {
        "Income Status": income_status,
        "Family Quotient Reduction (€)": family_quotient_reduction,
        "Childcare Credit (€)": childcare_credit,
        "Home Help Credit (€)": home_help_credit,
        "Renovation Credit (€)": renovation_credit,
        "Total Tax Credits (€)": total_credits
    }

# Example interactive usage
print("\n--- French Tax Deduction Calculator ---")
income = float(input("Enter your income (€): "))
num_half_shares = float(input("Enter number of half-shares in household (e.g., 2 for single, 3 for 1 child): "))
childcare_expense = float(input("Enter childcare expenses (€): "))
home_help_expense = float(input("Enter home help services expenses (€): "))
renovation_input = input("Did you make energy-saving home improvements (yes/no)? ").strip().lower()
renovation_eligible = renovation_input == "yes"

result = calculate_tax_deductions(income, num_half_shares, childcare_expense, home_help_expense, renovation_eligible)

print("\n--- Tax Deduction Summary ---")
for key, value in result.items():
    print(f"{key}: {value}")