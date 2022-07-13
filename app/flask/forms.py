from flask_wtf import FlaskForm
from wtforms import StringField, DateField,  SubmitField, SelectField
from wtforms.validators import DataRequired

popular_currencies = ["eur", "usd", "sgd", "jpy", "gbp", "chf", "aud", "cad", "cny"  ]

class QueryForm(FlaskForm):
    # DataRequired validator simply checks if field has any input at all
    #currency = StringField('Currency', validators=[DataRequired()])
    currency = SelectField(label='State', choices=popular_currencies)
    date = DateField('entrydate', format='%Y-%m-%d', validators=[DataRequired()] )
    submit = SubmitField('Get Rates')