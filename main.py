import assets as asset_module
import liabilities as liabilities_module
import CONSTS as CONSTS

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
    cur_age = None
    while cur_age is None: 
        age = int(input("Please input current age: "))
        if age < 0: 
            print("Please enter a valid age!")
            age = None
    ret_age = None
    while ret_age is None: 
        ret_age = int(input("Please enter your desired retirement age: "))
        if ret_age < 0: 
            print("Please enter a valid age!")
            ret_age = None
    ret_yearly_spending = None
    while ret_yearly_spending is None: 
        ret_yearly_spending = float(input("Please enter how many dollars per year you'd like to spend/live off of in retirement: "))
        if ret_yearly_spending < 0: 
            print("Please enter a valid value!")
            ret_yearly_spending = None
    ret_leftover = None
    while ret_leftover is None: 
        ret_leftover = float(input("Please enter how much money (in total net worth) you'd like to leave behind: "))
        if ret_leftover < 0: 
            print("That's not very ambitious... please enter a valid value")
            ret_leftover = None
    death_age = 90
    avg_return = 0.9*CONSTS.short_tbill_return + 0.1*CONSTS.market_return
    ret_years = death_age - ret_age
    ret_funds = (ret_leftover - (-ret_yearly_spending/avg_return)*(1-(1+avg_return)**(-ret_years)))/((1+avg_return)**ret_years) # test this
    print(f"Assuming a safe death age of {death_age} and 90% investment into short-term treasury bills at retirement (giving an average yearly return of {avg_return}), we estimate you'll need about ${ret_funds} by the time you retire.")

    # Create financial goals list
    # Identify risk tolerance

if __name__=="__main__": 
    gather_financial_info()