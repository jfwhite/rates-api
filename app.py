from flask import Flask, request, jsonify
import sqlite3

app = Flask('RatesAPI')

@app.route('/', methods=['POST'])
def get_rates_for_loan():
    data = request.json
    maturity_date = data["maturity_date"]
    reference_rate = data["reference_rate"]
    rate_floor = data["rate_floor"]
    rate_ceiling = data["rate_ceiling"]
    rate_spread = data["rate_spread"]
    
    connection = sqlite3.connect('rates.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT date, {reference_rate.lower()} from rates where date < '{maturity_date}'")
    return jsonify([
        {
            "date": date,
            "rate": apply_spread_floor_and_ceiling(rate, rate_spread, rate_floor, rate_ceiling) 
        }
        for date, rate in cursor.fetchall()
    ])

def apply_spread_floor_and_ceiling(rate, rate_spread, rate_floor, rate_ceiling):
    return_rate = rate + rate_spread
    if return_rate < rate_floor:
        return rate_floor
    elif return_rate > rate_ceiling:
        return rate_ceiling
    else:
        return return_rate
    
