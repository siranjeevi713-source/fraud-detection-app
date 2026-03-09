import pandas as pd

def detect_fraud(df):

    suspicious = []

    for i, row in df.iterrows():

        if row["amount"] > 40000:
            suspicious.append(row)

    return pd.DataFrame(suspicious)
