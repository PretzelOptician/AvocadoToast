import assets as asset_module
import liabilities as liabilities_module
import goals as goals_module
import financial_calculator as financial_calculator
import CONSTS as CONSTS

class FinancialInfo(): 
    def __init__(self, income: float, expenses: float, taxes: float, pct_budget: float, assets: list[asset_module.Asset], liabilities: list[liabilities_module.Liability], financial_goals: list[goals_module.FinancialGoal], match_401k: int, cur_age: int, ret_age: int, ret_yearly_spending: float, ret_leftover: float, ret_funds: float):
        self.income = income
        self.expenses = expenses
        self.taxes = taxes
        self.pct_budget = pct_budget
        self.assets = assets
        self.liabilities = liabilities
        self.financial_goals = financial_goals
        self.match_401k = match_401k
        self.cur_age = cur_age
        self.ret_age = ret_age
        self.ret_yearly_spending = ret_yearly_spending
        self.ret_leftover = ret_leftover
        self.ret_funds = ret_funds

    def calculate_return_table(self): 
        #calculate net worth
        total_assets = 0
        for asset in self.assets: 
            total_assets += asset.value
        total_liabilities = 0
        for liability in self.liabilities: 
            total_liabilities += liability.value
        net_worth = total_assets - total_liabilities
            
        sorted_goals = sorted(self.financial_goals, key=lambda x: x.years) #TODO: reverse this (don't know how without google)
        net_worth_inc_needed = self.ret_funds - net_worth
        for goal in sorted_goals: 
            if goal.asset is None: 
                net_worth_inc_needed += goal.amount
        return_req = financial_calculator.get_return_from_fv_and_pv(net_worth+net_worth_inc_needed, net_worth, ret_age-cur_age)
        print(f"Your net worth is approximately {net_worth} and the amount it will need to increase to get your retirement funds is {net_worth_inc_needed}! You have {ret_age-cur_age} years to accomplish this, so you will need to average a return of {return_req}.")
        return_table = {self.ret_age-self.cur_age: return_req}
        # this part is a little complicated. We are basically searching the average return required to hit all previous goals and if any aree higher, a higher return will be needed in that period of time. 
        for goal in sorted_goals:
            inc_needed = goal.amount - net_worth
            for goal2 in sorted_goals: 
                if goal2.years > goal.years: break
                if goal2.asset is None: 
                    inc_needed += goal2.amount
            new_return_req = financial_calculator.get_return_from_fv_and_pv(net_worth+inc_needed, net_worth, goal.years)
            if new_return_req > return_req: 
                return_req = new_return_req
                return_table[goal.years] = return_req
        return return_table

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
        assets: list[asset_module.Asset] = asset_module.register_assets()
    else: 
        assets = []
    yn = input("Do you have any liabilities/debts? (y/n): ")
    if yn == 'y': 
        liabilities: list[liabilities_module.Liability] = liabilities_module.register_liabilities()
    else: 
        liabilities = []
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
        cur_age = int(input("Please input current age: "))
        if cur_age < 0: 
            print("Please enter a valid age!")
            cur_age = None
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
    avg_risk = 0.9*CONSTS.short_tbill_risk + 0.1*CONSTS.market_risk
    ret_years = death_age - ret_age
    ret_funds = (ret_leftover - (-ret_yearly_spending/avg_return)*(1-(1+avg_return)**(-ret_years)))/((1+avg_return)**ret_years) # test this
    print(f"Assuming a safe death age of {death_age} and 90% investment into short-term treasury bills at retirement (giving an average yearly return of {avg_return}), we estimate you'll need about ${ret_funds} by the time you retire.")
    retirement_goal = goals_module.FinancialGoal(years=(ret_age-cur_age), amount=ret_funds, name="Retirement", asset=asset_module.Asset(name="Retirement Fund", amount=ret_funds, avg_return=avg_return, avg_risk=avg_risk, liquid=True))

    # Create financial goals list
    yn = input("Do you have any financial goals? (y/n): ")
    if yn == 'y': 
        goals: list[goals_module.FinancialGoal] = goals_module.register_goals()
    else: 
        goals = []
    goals.append(retirement_goal)
    user_info = FinancialInfo(income, expenses, taxes, pct_budget, assets, liabilities, goals, match_401k, cur_age, ret_age, ret_yearly_spending, ret_leftover, ret_funds)
    return user_info

if __name__=="__main__": 
    info = gather_financial_info()
    #save with pickl