from flask import Flask, render_template
from datetime import datetime
from eps import get_eps, get_acc_eps, get_coms, get_com_eps
import json

app = Flask(__name__)


@app.route("/current-EPS-charts")
def current_EPS_charts():
    coms = get_coms()
    return render_template("eps-charts.html", coms=coms)


@app.route("/acc-EPS-data")
def acc_EPS_data():
    acc_columns, acc_values, acc_target = get_acc_eps()
    acc_company = [acc_value[0] for acc_value in acc_values]
    acc_current_EPS = [acc_value[-2] for acc_value in acc_values]
    acc_current_rank = [acc_value[-1] for acc_value in acc_values]
    acc_sorted_eps = sorted(acc_values, key=lambda x: x[-2])
    print(acc_sorted_eps)
    # 取得第一名資料
    acc_highest = {
        "acc_company": acc_sorted_eps[-1][0],
        "acc_current_EPS": acc_sorted_eps[-1][-2],
        "acc_current_rank": acc_sorted_eps[-1][-1],
    }
    # 取得第二名資料
    acc_second = {
        "acc_company": acc_sorted_eps[-2][0],
        "acc_current_EPS": acc_sorted_eps[-2][-2],
        "acc_current_rank": acc_sorted_eps[-2][-1],
    }
    # 取得本公司資料
    acc_point = {
        "acc_company": acc_target[0][0],
        "acc_current_EPS": acc_target[0][-2],
        "acc_current_rank": acc_target[0][-1],
    }
    acc_result = json.dumps(
        {
            "acc_company": acc_company,
            "acc_current_EPS": acc_current_EPS,
            "acc_current_rank": acc_current_rank,
            "acc_highest": acc_highest,
            "acc_second": acc_second,
            "acc_point": acc_point,
        },
        ensure_ascii=False,
    )
    return acc_result


@app.route("/current-EPS-data", methods=["GET"])  # 如果是很私密的資料要改成POST
def current_EPS_data():
    columns, values, target = get_eps()
    company = [value[0] for value in values]
    current_EPS = [value[6] for value in values]
    current_rank = [value[7] for value in values]
    sorted_eps = sorted(values, key=lambda x: x[6])
    print(sorted_eps)
    # 取得第一名資料
    highest = {
        "company": sorted_eps[-1][0],
        "current_EPS": sorted_eps[-1][6],
        "current_rank": sorted_eps[-1][7],
    }
    # 取得第二名資料
    second = {
        "company": sorted_eps[-2][0],
        "current_EPS": sorted_eps[-2][6],
        "current_rank": sorted_eps[-2][7],
    }
    # 取得本公司資料
    point = {
        "company": target[0][0],
        "current_EPS": target[0][6],
        "current_rank": target[0][7],
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


@app.route("/com-EPS-data/<com>")
def com_EPS_data(com):
    columns, values = get_com_eps(com)
    capital = [value[1] for value in values]
    gains = [value[2] for value in values]
    pre_gains = [value[3] for value in values]
    acc_gains = [value[9] for value in values]

    result = json.dumps(
        {
            "capital": capital,
            "gains": gains,
            "pre_gains": pre_gains,
            "acc_gains": acc_gains,
        },
        ensure_ascii=False,
    )
    return result


@app.route("/")
def eps_table():
    columns, values, target = get_eps()
    # print(columns, values,target)
    return render_template("eps.html", columns=columns, values=values)


# print(current_EPS_data())


app.run(debug=True)
