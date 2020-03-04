from flask import Flask, render_template
from datetime import datetime
from learn_web.webapp.weather import weather_by_city
from learn_web.webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route("/")
    def index():
        title = "Новости python"
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

    return app

    @app.route("/stat")
    def stat():
        return {'Status': True, 'Time': datetime.now()}

#    export FLASK_APP=webapp && export FLASK_ENV=development && flask run

