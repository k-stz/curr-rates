from flask_wtf import FlaskForm
from wtforms import DateField,  SubmitField, SelectField
from wtforms.validators import DataRequired

popular_currencies = ["eur", "usd", "sgd", "jpy", "gbp", "chf", "aud", "cad", "cny"  ]

class QueryForm(FlaskForm):
    currency = SelectField(label='Currency', choices=popular_currencies)
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()] )
    submit = SubmitField('Get Rates')