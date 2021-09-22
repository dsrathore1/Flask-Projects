from flask import Flask
from flask.helpers import url_for
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.register_blueprint(views, url_prefix="/home")
app.register_blueprint(views, url_prefix="/route")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
