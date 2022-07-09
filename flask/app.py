# flask_web/app.py

from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="World")

# https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@{apiVersion}/{date}/{endpoint}
# example:
# https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/2020-11-24/currencies/eur.min.json

# date: 'latest' or YYYY-MM-DD
# TODO: historical rates oly available for some dates and some may be missing

# TODO: fallback
# endpoint:
# support GET-Method and .min.json or .json format (each work as fallback!)

# available currencies: 
# prettified json: https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json
# minified iwth .min.json extension

@app.route('/eur')
def rate():
    currency = 'eur'
    data = get_rate("eur", "2020-11-24")
    # x = currencies
    # y = value
    labels, values = get_labels_values(data)
    # prepend reference curency, so it shows up first
    labels = [currency] + labels
    values = [1.0] + values
    return render_template('chart.html', currency=currency, labels=labels, values=values)

def get_labels_values(data):
    return list(data.keys()), list(data.values())

# TODO add caching
def get_rate(currency, date):
    # TODO validate date and currency
    # TODO add fallback url logic
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date}/currencies/{currency}.min.json"
    with urllib.request.urlopen(url) as response:
        # data is a dict
        data = json.loads(response.read().decode())
    return data[currency]

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

