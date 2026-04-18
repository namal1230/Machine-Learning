import numpy as np

def total_spending(df):
    return np.sum(df["Amount"])

def category_spending(df):
    return df.groupby("Category")["Amount"].sum()

def monthly_trend(df):
    return df.groupby("Month")["Amount"].sum()

def average_spending(df):
    return np.mean(df["Amount"])