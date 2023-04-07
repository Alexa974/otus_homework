"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    # return "It's Index pages"
    return flask.render_template('index.html')


@app.route("/about/")
def about():
    # return "Flask is a web framework that offers tools, libraries, " \
    #         "and technologies suitable for building a web application. " \
    #         "This web application can come in the form of web pages, " \
    #         "blogs, or even an extensive web-based calendar app or " \
    #         "a commercial site. Flask is one of the best micro-frameworks, " \
    #         "as it has little to no dependencies on external libraries."
    return flask.render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
