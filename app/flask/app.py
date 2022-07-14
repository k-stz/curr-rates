from flask import Flask, render_template, flash, redirect
import os, urllib.request, json
from forms import QueryForm
app = Flask(__name__)

class Config(object):
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

@app.route('/currencies')
def get_currencies():
    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
    with urllib.request.urlopen(url) as response:
        # TODO catch HTTPError here and render Errorpage
        data = json.loads(response.read().decode())
    return data

@app.route('/<string:currency>/<string:date>')
def rate(currency, date):
    data = get_rate(currency, date)
    data = filter_popular(data, currency)
    labels, values = get_labels_values(data)
    return render_template('chart.html', labels=labels, values=values, currency=currency, date=date )



def filter_popular(data_dict, chosen_currency):
    popular_currencies = ["eur", "usd", "sgd", "jpy", "gbp", "chf", "aud", "cad", "cny"  ]
    return { currency: data_dict[currency] for currency in popular_currencies if currency != chosen_currency }

def get_labels_values(data):
    return list(data.keys()), list(data.values())

def get_rate(currency, date):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date}/currencies/{currency}.min.json"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data[currency]

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

