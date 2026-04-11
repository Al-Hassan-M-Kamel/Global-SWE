from flask import Flask, request, render_template
from flask_babel import Babel
from flask_babel import gettext as _
from datetime import datetime
from flask_babel import format_datetime


app = Flask(__name__)

def get_locale():

    return request.accept_languages.best_match(["en", "fr", "ar"])

babel = Babel(app, locale_selector = get_locale)


@app.route('/')
def Index():

    msg = _("Welcome to our app...")

    return render_template('index.html', msg=msg, count=1, d=datetime(1987, 3, 5, 17, 12))


if __name__ == '__main__':
    app.run(debug=True)