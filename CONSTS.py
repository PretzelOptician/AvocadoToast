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

real_estate_return = 0.106
real_estate_risk = 0.087