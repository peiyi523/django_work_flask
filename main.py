from flask import Flask, render_template
from datetime import datetime
from eps import get_eps
import json

app = Flask(__name__)


@app.route("/current-EPS-charts")
def current_EPS_charts():
    return render_template("eps-charts.html")


@app.route("/current-EPS-data", methods=["GET"])  # 如果是很私密的資料要改成POST
def current_EPS_data():
    columns, values = get_eps()
    company = [value[0] for value in values]
    current_EPS = [value[6] for value in values]

    result = json.dumps(
        {"company": company, "current_EPS": current_EPS}, ensure_ascii=False
    )
    return result


@app.route("/")
def eps_table():
    columns, values = get_eps()
    # print(columns, values)
    return render_template("eps.html", columns=columns, values=values)


print(current_EPS_data())
app.run(debug=True)
