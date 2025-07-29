
import requests
import pandas as pd
import streamlit as st

def fetch_fx_daily(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={symbol[:3]}&to_symbol={symbol[3:]}&outputsize=compact&apikey={api_key}"
    r = requests.get(url)
    data = r.json().get("Time Series FX (Daily)", {})
    df = pd.DataFrame(data).T
    df.columns = ['open', 'high', 'low', 'close']
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df
