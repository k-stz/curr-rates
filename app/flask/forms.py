from flask_wtf import FlaskForm
from wtforms import DateField,  SubmitField, SelectField
from wtforms.validators import DataRequired

popular_currencies = ["eur", "usd", "sgd", "jpy", "gbp", "chf", "aud", "cad", "cny"  ]

class QueryForm(FlaskForm):
    currency = SelectField(label='State', choices=popular_currencies)
    date = DateField('entrydate', format='%Y-%m-%d', validators=[DataRequired()] )
    submit = SubmitField('Get Rates')