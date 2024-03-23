import pandas as pd


def get_eps():
    df = pd.read_excel("C:/Users/PEIYI/Dropbox/PC/Desktop/django/參考資料2.xlsx")
    df = round(df, 2).dropna()
    columns = df.columns.tolist()
    values = df.values.tolist()
    key = "統一證券"
    target = [value for value in values if value[0] == key]
    return columns, values, target


if __name__ == "__main__":
    print(get_eps())
