'''
This document contains the constant values used for the asset type presets. 
This is updated using latest historical information as of late 2023. 
'''

# numbers based off VOO (Vanguard S&P 500)
market_return = 0.1026
market_risk = 0.175

# numbers from treasury
short_tbill_return = 0.0481
short_tbill_risk = 0 # assumption of zero risk for treasury bills (if the US treasury defaults, you have worse things to worry about)

long_tbill_return = 0.0405 # (yield curve negative, wow!)
long_tbill_risk = 0 # assumption of zero risk for treasury bills (if the US treasury defaults, you have worse things to worry about)

cash_return = 0.0046 # average interest for savings accounts, from cnn

real_estate_return = 0.106 # https://www.mdpi.com/1911-8074/15/8/369#:~:text=Including%20idiosyncratic%20and%20illiquidity%20risks,comparable%20to%20the%20S%26P%20500.
real_estate_risk = 0.087 

car_return = -0.0802 # https://www.carsdirect.com/auto-loans/what-is-the-average-car-depreciation-rate
car_risk = 0.039 # this number was impossible to find. but I basically just took the 15% depreciation in first year and roughly 6.3% depreciation for the following years and found the SD off that