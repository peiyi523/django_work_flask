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
    columns, values, target = get_eps()
    company = [value[0] for value in values]
    current_EPS = [value[6] for value in values]
    current_rank = [value[-1] for value in values]
    # 取得第一名資料及本公司資料
    sorted_eps = sorted(values, key=lambda x: x[6])
    print(sorted_eps)
    highest = {
        "company": sorted_eps[-1][0],
        "current_EPS": sorted_eps[-1][6],
        "current_rank": sorted_eps[-1][-1],
    }

    second = {
        "company": sorted_eps[-2][0],
        "current_EPS": sorted_eps[-2][6],
        "current_rank": sorted_eps[-2][-1],
    }

    # 本公司資料
    point = {
        "company": target[0][0],
        "current_EPS": target[0][6],
        "current_rank": target[0][-1],
    }
    result = json.dumps(
        {
            "company": company,
            "current_EPS": current_EPS,
            "current_rank": current_rank,
            "highest": highest,
            "second": second,
            "point": point,
        },
        ensure_ascii=False,
    )
    return result


@app.route("/")
def eps_table():
    columns, values, target = get_eps()
    # print(columns, values)
    return render_template("eps.html", columns=columns, values=values)


print(current_EPS_data())


app.run(debug=True)
