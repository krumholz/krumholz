from flask import Flask, render_template
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app, permanent=True)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/sortable')
def sortable():
    return render_template("sortable.html")


if __name__ == '__main__':
    app.run(debug=True)
