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

@app.route('/currencies')
def get_currencies():
    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
    with urllib.request.urlopen(url) as response:
        # data is a dict
        # TODO catch HTTPError here and render Errorpage
        data = json.loads(response.read().decode())
    return data



@app.route('/<string:currency>/<string:date>')
def rate(currency, date):
    # eur/2020-11-24
    print(f"currency:{currency} date:{date}")
    #currency = 'eur'
    #date = "2020-11-24"
    data = get_rate(currency, date)
    data = filter_popular(data, currency)
    # x = currencies
    # y = value
    labels, values = get_labels_values(data)
    # prepend reference curency, so it shows up first
    labels = labels
    values = values
    return render_template('chart.html', labels=labels, values=values, currency=currency, date=date )

popular_currencies = ["eur", "usd", "sgd", "jpy", "gbp", "chf", "aud", "cad", "cny"  ]
# popular_currencies = ["eur", "usd", "sgd", "gbp", "chf", "aud", "cad", "cny"  ]

def filter_popular(data_dict, chosen_currency):
    return { currency: data_dict[currency] for currency in popular_currencies if currency != chosen_currency }

def get_labels_values(data):
    return list(data.keys()), list(data.values())

# TODO add caching
def get_rate(currency, date):
    # TODO validate date and currency
    # TODO add fallback url logic
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date}/currencies/{currency}.min.json"
    with urllib.request.urlopen(url) as response:
        # data is a dict
        # TODO catch HTTPError here and render Errorpage
        data = json.loads(response.read().decode())
    return data[currency]

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

