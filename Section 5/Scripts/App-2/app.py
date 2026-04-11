
from flask import Flask
from flask_babel import format_datetime, Babel
from flask_babel import format_currency, format_number
from datetime import datetime


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

app.test_request_context().push()

print(format_number(1234567.89))

print(format_currency(49.99, 'EGP'))





print(format_datetime(datetime(1987, 3, 5, 17, 12), 'full'))
print(format_datetime(datetime(1987, 3, 5, 17, 12), 'short'))
print(format_datetime(datetime(1987, 3, 5, 17, 12), 'dd mm yyyy'))

