from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def get_eps():
    eps = {"元大證券": {"資本額": "659", "2月稅後損益 ": "12", "2月稅後EPS": "0.179"}}
    return render_template("eps.html", eps=eps)


app.run(debug=True)
