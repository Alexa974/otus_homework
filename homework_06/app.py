import os

import flask
from flask_migrate import Migrate

from models import db
from views.posts import posts_app

app = flask.Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True
app.register_blueprint(posts_app, url_prefix="/posts")

CONFIG_OBJ_PATH = 'config.{}'.format(os.getenv("CONFIG", "ProductionConfig"))
print(CONFIG_OBJ_PATH)
app.config.from_object(CONFIG_OBJ_PATH)

db.init_app(app)

migrate = Migrate(app, db)



@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/about/")
def about():
    return flask.render_template('about.html')


if __name__ == '__main__':
    app.run()
