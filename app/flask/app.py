# flask_web/app.py

from flask import Flask, render_template, flash, redirect
import os, urllib.request, json
from forms import QueryForm
app = Flask(__name__)

class Config(object):
    # `SECRET_KEY` is used by Flask extension as a cryptographic key 
    # to generate signatures or tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-default-secret-key'

app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        currency = form.currency.data
        date = form.date.data
        flash(f"Query submitted:{currency} on {date}")
        return redirect(f"{currency}/{date}")
    return render_template('index.html', form=form)

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

