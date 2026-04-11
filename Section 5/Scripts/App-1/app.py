from flask import Flask, request, render_template
from flask_babel import Babel
from flask_babel import gettext as _
from flask_babel import format_currency, format_number, format_datetime
from datetime import datetime

def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'ar'])

app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def Index():
    msg = _('Welcome To our app...')

    return render_template('index.html', msg=msg, count=1, d=datetime(1987, 3, 5, 17, 12))


if __name__ == '__main__':
    app.run(debug=True)