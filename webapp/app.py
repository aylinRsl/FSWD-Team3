from flask import Flask, render_template

app = Flask(__name__)
# homepage
@app.route("/")
def home():
    return render_template("base.html")