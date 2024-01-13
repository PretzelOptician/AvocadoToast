def get_return_from_fv_and_pv(fv: float, pv: float, years: float, monthly_budget: float):
    # present_value_of_cash_flows = pv
     
    return ((fv/pv)**(1/years) - 1)
    # TODO: factor in monthly budget