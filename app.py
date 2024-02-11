from flask import Flask, render_template, request
import assets as asset_module
import liabilities as liabilities_module
import goals as goals_module
import financial_calculator as financial_calculator
import CONSTS as CONSTS
import pickle
import os
from copy import deepcopy
from typing import List as list
from datetime import datetime, timedelta
import main as main_module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result(): 
    if request.method == 'POST':
        income = float(request.form['income'])
        expenses = float(request.form['expenses'])
        taxes = float(request.form['taxes'])
        pct_budget = float(request.form['pct_budget'])

        # handle assets
        assets = []
        if request.form.getlist('asset_name[]'):
            asset_names = request.form.getlist('asset_name[]')
            asset_values = request.form.getlist('asset_value[]')
            asset_returns = request.form.getlist('asset_return[]')
            asset_risks = request.form.getlist('asset_risks[]')
            asset_liquid = request.form.getlist('asset_liquid[]')
            for name, value, ret, risk, liquid in zip(asset_names, asset_values, asset_returns, asset_risks, asset_liquid):
                if name: 
                    assets.append(asset_module.Asset(name, float(value), float(ret), float(risk), liquid))

        # handle liabilities
        liabilities = []
        if request.form.getlist('liability_name[]'): 
            liability_names = request.form.getlist('liability_name[]')
            liability_values = request.form.getlist('liability_value[]')
            liability_interest = request.form.getlist('liability_interest[]')
            for name, value, interest in zip(liability_names, liability_values, liability_interest):
                if name: 
                    liabilities.append(liabilities_module.Liability(name, float(value), float(interest)))

        # handle goals
        goals = []
        if request.form.getlist('goal_name[]'): 
            goal_names = request.form.getlist('goal_name[]')
            goal_years = request.form.getlist('goal_year[]')
            goal_amount = request.form.getlist('goal_amount[]')
            for name, year, amount in zip(goal_names, goal_years, goal_amount): 
                if name: 
                    goals.append(goals_module.FinancialGoal(name, float(year), float(amount)))

        cur_age = float(request.form['cur_age'])
        ret_age = float(request.form['ret_age'])
        ret_yearly_spending = float(request.form['ret_yearly_spending'])
        ret_leftover = float(request.form['ret_leftover'])

        # net_income = income - taxes - expenses
        death_age = 90
        avg_return = 0.9*CONSTS.short_tbill_return + 0.1*CONSTS.market_return
        avg_risk = 0.9*CONSTS.short_tbill_risk + 0.1*CONSTS.market_risk
        ret_years = death_age - ret_age
        ret_funds = financial_calculator.calc_retirement_funds(ret_leftover, ret_yearly_spending, avg_return, ret_years)
        retirement_goal = goals_module.FinancialGoal(years=(ret_age-cur_age), amount=ret_funds, name="Retirement", asset=asset_module.Asset(name="Retirement Fund", value=ret_funds, avg_return=avg_return, risk=avg_risk, liquid=True))
        goals.append(retirement_goal)

        user_info = main_module.FinancialInfo(income, expenses, taxes, pct_budget, assets, liabilities, goals, None, cur_age, ret_age, ret_yearly_spending, ret_leftover, ret_funds)

        results = user_info.create_plan()
        return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)