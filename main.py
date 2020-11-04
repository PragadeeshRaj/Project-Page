import projects  # projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())


# connects /hello path of server to render hello.html
@app.route('/fundamentals/')
def hello_route():
    return render_template("fundamentals.html", projects=projects.setup())


# connects /flask path of server to render flask.html
@app.route('/calculator/')
def flask_route():
    return render_template("calculator.html", projects=projects.setup())


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='5000', host='127.0.0.1')

