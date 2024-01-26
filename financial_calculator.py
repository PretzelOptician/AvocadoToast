from scipy.optimize import newton
from math import log as ln

def get_return_from_fv_and_pv(fv: float, pv: float, years: float, monthly_budget: float):
    def objective_function(ret):
        return get_fv_comp_int(ret, pv, years, monthly_budget) - fv

    ret_guess = 0.0001
    ret_solution = newton(objective_function, ret_guess)

    return ret_solution


def get_fv_comp_int(ret: float, pv: float, years: float, monthly_budget: float): 
    return (12*monthly_budget)*(((1+ret)**years-1)/ret) + pv*(1+ret)**years

def calc_retirement_funds(ret_leftover, ret_yearly_spending, avg_return, ret_years): 
    return ret_leftover/((1+avg_return)**ret_years) + (ret_yearly_spending/avg_return) * (1 - (1/(1+avg_return)**ret_years)) * (1+avg_return)

def time_to_pay_off_loan(balance, payment, rate): 
    return -ln(1-(rate*balance/payment))/ln(1+rate)

if __name__=="__main__": 
    # testing
    print(time_to_pay_off_loan(10000, 1200, 0.1))