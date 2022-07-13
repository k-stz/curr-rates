from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    # DataRequired validator simply checks if field has any input at all
    currency = StringField('Currency', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    #currencies = StringField('Compare with', validators=[DataRequired()))
    submit = SubmitField('Get Rates')