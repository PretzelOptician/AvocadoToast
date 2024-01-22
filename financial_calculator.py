def get_return_from_fv_and_pv(fv: float, pv: float, years: float, monthly_budget: float):
    # present_value_of_cash_flows = pv
     
    return ((fv/pv)**(1/years) - 1)
    # TODO: factor in monthly budget

def calc_retirement_funds(ret_leftover, ret_yearly_spending, avg_return, ret_years): 
    return ret_leftover/((1+avg_return)**ret_years) + (ret_yearly_spending/avg_return) * (1 - (1/(1+avg_return)**ret_years)) * (1+avg_return)