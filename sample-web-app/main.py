from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, SmartNinja23!"

@app.route("/kontostand")
def kontostand():
    kontostand=550.09
    return "Hello, SmartNinja dein Konto beträgt: " +str(kontostand)

@app.route("/about_me")
def about_me():
    return render_template("about.html")

if __name__ =='__main__':
    app.run()