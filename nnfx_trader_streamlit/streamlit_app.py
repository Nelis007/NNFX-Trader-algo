
import streamlit as st
import pandas as pd
from utils import fetch_fx_daily
from indicators import calculate_kama, calculate_roc, calculate_atr, calculate_di

st.title("NNFX Forex Signal Assistant")

api_key = st.secrets["ALPHA_VANTAGE_API_KEY"]
symbols = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD"]
symbol = st.selectbox("Select Currency Pair", symbols)

df = fetch_fx_daily(symbol, api_key)
df['KAMA'] = calculate_kama(df['close'])
df['ROC'] = calculate_roc(df['close'])
df['ATR'] = calculate_atr(df['high'], df['low'], df['close'])
df['+DI'], df['-DI'] = calculate_di(df['high'], df['low'], df['close'])

latest = df.iloc[-1]
signal = "Hold"
if latest['KAMA'] > df['KAMA'].iloc[-2] and latest['+DI'] > latest['-DI']:
    signal = "Buy"
elif latest['KAMA'] < df['KAMA'].iloc[-2] and latest['-DI'] > latest['+DI']:
    signal = "Sell"

st.metric("Signal", signal)
st.line_chart(df[['close', 'KAMA']].dropna())
