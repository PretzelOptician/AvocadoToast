import CONSTS as CONSTS

asset_types_instructions = '''
Now, please enter what type of asset this is. 
Note that these are just presets. 
If you want, you can pick 6 to enter a custom asset, but you must know the expected annual return and expected standard deviation on that return. 
Also, advanced users may change CONSTS.py to change the presets.
Do NOT include illiquid depreciating assets like cars. 
1 - Market fund (such as S&P 500)
2 - Short term treasury bonds
3 - Long term treasury bonds
4 - Cash
5 - Real estate/house
6 - Car
7 - Custom asset
'''

class Asset(): 
    def __init__(self, name: str, value: float, avg_return: float, risk: float, liquid: bool):
        self.name = name
        self.value = value
        self.avg_return = avg_return
        self.risk = risk
        self.liquid = liquid

class MarketFund(Asset): 
    def __init__(self, name: str, value: float): 
        self.name = name
        self.value = value
        self.avg_return = CONSTS.market_return
        self.risk = CONSTS.market_risk
        self.liquid = True

class ShortTermTreasury(Asset): 
    def __init__(self, name: str, value: float): 
        self.name = name
        self.value = value
        self.avg_return = CONSTS.short_tbill_return
        self.risk = CONSTS.short_tbill_risk
        self.liquid = True

class LongTermTreasury(Asset): 
    def __init__(self, name: str, value: float): 
        self.name = name
        self.value = value
        self.avg_return = CONSTS.long_tbill_return
        self.risk = CONSTS.long_tbill_risk
        self.liquid = True

class Cash(Asset): 
    def __init__(self, name: str, value: float): 
        self.name = name
        self.value = value
        self.avg_return = CONSTS.cash_return
        self.risk = 0 # by definition, cash has no risk
        self.liquid = True

class RealEstate(Asset): 
    def __init__(self, name: str, value: float): 
        self.name = name
        self.value = value
        self.avg_return = CONSTS.real_estate_return
        self.risk = CONSTS.real_estate_risk
        self.liquid = False

class Vehicle(Asset):
    def __init__(self, name: str, value: float): 
        self.name = name
        self.value = value
        self.avg_return = CONSTS.car_return
        self.risk = CONSTS.car_return
        self.liquid = False

def register_assets(): 
    assets = []
    print("Now, we will register your assets. We will start with asset 1, and you can list as many as you want. Pick from the options we give you or register your own custom asset. ")
    yn = 'y'
    while yn == 'y': 
        new_asset = register_single_asset()
        assets.append(new_asset)
        yn = input("Would you like to register another asset? (y/n): ")
    return assets
    
def register_single_asset(value: float): 
    name = input("Please give your asset an identifiable name: ")
    print(asset_types_instructions)
    new_asset: Asset = None
    asset_type_id = int(input("Please enter the id you want (6 not working yet): "))
    if asset_type_id == 1: 
        new_asset = MarketFund(name, value)
    elif asset_type_id == 2: 
        new_asset = ShortTermTreasury(name, value)
    elif asset_type_id == 3: 
        new_asset = LongTermTreasury(name, value)
    elif asset_type_id == 4: 
        new_asset = Cash(name, value)
    elif asset_type_id == 5: 
        new_asset = RealEstate(name, value)
    elif asset_type_id == 6: 
        new_asset = Vehicle(name, value)
    elif asset_type_id == 7:
        ret = None
        while ret is None: 
            ret = float(input("Please enter the expected annual return of this asset AS A DECIMAL (e.g. 0.1 for 10%): "))
        risk = None
        while risk is None: 
            risk = float(input("Please enter the expected standard deviation of the return AS A DECIMAL (e.g. 0.1 for 10%): "))
            if risk < 0 or risk > 1: 
                print("Risk must be between 0 and 1!")
        liquid = False
        if input("Is this asset liquid (can it easily be converted into cash)? (y/n): ") == "y": 
            liquid = True
        new_asset = Asset(name, value, ret, risk, liquid)
    else: 
        print("Input not recognized. Restarting.")
    return new_asset