class Liability(): 
    def __init__(self, name: str, value: float, interest: float): 
        self.name = name
        self.value = value
        self.interest = interest

def register_liabilities(): 
    liabilities = []
    print("Now, we will register your debts/liabilities. We will start with debt 1, and you can list as many as you want. ")
    yn = 'y'
    while yn == 'y': 
        name = input("Please give your debt an identifiable name: ")
        value = None
        while value == None: 
            value = float(input("What's the balance of this debt: "))
            if value < 0: 
                print("Value can't be negative!")
                value = None
        interest = None
        while interest == None: 
            interest = float(input("What's the interest rate on this debt? Please enter as a decimal (e.g. 0.1 instead of 10%): "))
        liability = Liability(name, value, interest)
        liabilities.append(liability)
        yn = input("Would you like to register another liability? (y/n): ")
    return liabilities
    