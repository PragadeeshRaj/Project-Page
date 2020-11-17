import projects  # imports projects data from projects.py

from flask import Flask, render_template  # imports the render template

app = Flask(__name__)


@app.route('/')  # decorates the url with a route
def home_route():
    return render_template("home.html", projects=projects.setup())


@app.route('/fundamentals/')
def fundamental_route():
    return render_template("fundamentals.html", projects=projects.setup())
    # decoration passed through render_template of the setup in respective html file.


@app.route('/calculator/')
def calculator_route():
    return render_template("calculator.html", projects=projects.setup())


@app.route('/ayman/')
def ayman_route():
    return render_template("ayman.html", projects=projects.setup())


@app.route('/pragadeesh/')
def pragadeesh_route():
    return render_template("pragadeesh.html", projects=projects.setup())


@app.route('/brandon/')
def brandon_route():
    return render_template("brandon.html", projects=projects.setup())


@app.route('/ali/')
def ali_route():
    return render_template("ali.html", projects=projects.setup())


@app.route('/navodit/')
def navodit_route():
    return render_template("navodit.html", projects=projects.setup())


@app.route('/journal/')
def journal_route():
    return render_template("journal.html", projects=projects.setup())


if __name__ == "__main__":
    app.run(port='8080', host='66.172.116.112')
    # runs at IntelliJ port with LAN host
