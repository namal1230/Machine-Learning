import pandas as pd

def load_daa(file):
    df=pd.read_csv(file)

    df["Date"]=pd.to_datetime(df["Date"])
    df = df.dropna()
    df = df.drop_duplicates()

    df["Month"] = df["Date"].dt.to_period("M")
    df["Day"] = df["Date"].dt.day_name()

    return df