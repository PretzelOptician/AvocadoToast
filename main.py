import assets as asset_module
import liabilities as liabilities_module

def gather_financial_info(): 
    print("------------ STEP 1: BASIC FINANCIAL INFO ------------")
    income = None
    while income is None:
        income = float(input("Please enter your estimated total annual income, including investment income and debt taken ($): "))
        if income < 0: 
            print("Income can't be negative!")
            income = None
    expenses = None
    while expenses is None:
        expenses = float(input("Please enter your estimated annual expenses, excluding taxes ($): "))
        if expenses < 0: 
            print("Expenses can't be negative!")
            expenses = None
        if expenses > income: 
            print("Expenses can't be higher than income!")
            expenses = None
    taxes = None
    while taxes is None: 
        taxes = float(input("Please enter your estimated total taxes owed ($): "))
        if taxes < 0: 
            print("Taxes can't be negative!")
            taxes = None
        if taxes > income: 
            print("Taxes and expenses combined can't be higher than income!")
            taxes = None
    net_income = income - taxes - expenses
    print(f"You've specified that you have a net income (income - taxes - expenses) of ${round(net_income, 2)}.")
    pct_budget = None
    while pct_budget is None: 
        pct_budget = float(input("Please specify what percent of this net income you'd like to allocate to long-term financial goals (investment, retirement, paying off debt, etc). We recommend allocating as much money as you're comfortable with: "))
        if pct_budget < 0: 
            print("Percent can't be negative!")
            pct_budget = None
        if pct_budget > 100: 
            print("Percent can't be more than 100%!")
    investment_budget = pct_budget/100 * net_income
    # assets and liabilities
    yn = input("Do you have any assets? (y/n): ")
    if yn == 'y': 
        assets = asset_module.register_assets()
    else: 
        assets = []
    yn = input("Do you have any liabilities/debts? (y/n): ")
    if yn == 'y': 
        liabilities = liabilities_module.register_liabilities()
    else: 
        liabiltiies = []
    match_401k = None
    while match_401k is None: 
        if input("Does your employer provide you with a 401k contribution match? (y/n): ") == 'y': 
            match_401k = int(input("Up to how many dollars per year does your employer match your 401k contribution?: "))
            if match_401k < 0: 
                print("Match number cannot be negative!")
                match_401k = None
    print("------------ STEP 2: FINANCIAL GOALS ------------")
    # Ask current and retirement age (investment horizon)
    # Create financial goals list
    # Identify risk tolerance

if __name__=="__main__": 
    gather_financial_info()