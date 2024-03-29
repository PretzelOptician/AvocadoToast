import assets as assets_module

class FinancialGoal(): 
    def __init__(self, years, amount, name, asset: assets_module.Asset): 
        self.years = years
        self.amount = amount
        self.name = name
        self.asset = asset

def register_goals(): 
    goals: list[FinancialGoal] = []
    print("Now, we will register your short and long term financial goals, apart from retirement. This can be anything from owning a house to taking a nice vacation. We will start with goal 1, and you can list as many as you want. ")
    yn = 'y'
    while yn == 'y': 
        goal = register_single_goal()
        goals.append(goal)
        yn = input("Would you like to register another financial goal? (y/n): ")
    return goals

def register_single_goal(): 
    name = input("Please give your goal an identifiable name: ")
    amount = None
    while amount == None: 
        amount = float(input("What's the amount that you need to save for this goal: "))
        if amount < 0: 
            print("Amount can't be negative!")
            amount = None
    years = None
    while years == None: 
        years = float(input("How soon, in years, do you need the money by: "))
    yn2 = input("Is the goal to own a financial asset (such as a car or house)? Type 'n' if the money disappears after you reach the goal (such as a vacation). y/n: ")
    if yn2 == 'y': 
        asset = assets_module.register_single_asset(amount)
    else: 
        asset = None
    goal = FinancialGoal(years, amount, name, asset)
    return goal