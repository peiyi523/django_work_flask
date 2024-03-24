import pandas as pd

path = "C:/Users/PEIYI/Dropbox/PC/Desktop/django/參考資料2.xlsx"
df = None
key = "統一證券"


def get_eps():
    global df
    if df is None:
        df = pd.read_excel(path)
        df = round(df, 2).dropna()
    columns = df.columns.tolist()
    values = df.values.tolist()
    target = [value for value in values if value[0] == key]
    return columns, values, target


def get_acc_eps():
    global df
    if df is None:
        df = pd.read_excel(path)
        df = round(df, 2).dropna()
    acc_columns = df.columns.tolist()
    acc_values = df.values.tolist()
    acc_target = [acc_value for acc_value in acc_values if acc_value[0] == key]
    return acc_columns, acc_values, acc_target


def get_coms():
    global df
    if df is None:
        df = pd.read_excel(path)
        df = round(df, 2).dropna()
    coms = df["券商名稱"].unique()
    return coms


def get_com_eps(com):
    global df
    if df is None:
        df = pd.read_excel(path)
        df = round(df, 2).dropna()
    df1 = df.groupby("券商名稱").get_group(com)
    columns = df1.columns.tolist()
    values = df1.values.tolist()

    return columns, values


if __name__ == "__main__":
    print(get_eps())
    print(get_acc_eps())
    print(get_coms())
    print(get_com_eps("華南永昌"))
