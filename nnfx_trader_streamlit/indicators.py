
import pandas as pd

def calculate_kama(prices, er_period=10, fast=2, slow=30):
    change = abs(prices - prices.shift(er_period))
    volatility = prices.diff().abs().rolling(er_period).sum()
    er = change / volatility
    fast_sc = 2 / (fast + 1)
    slow_sc = 2 / (slow + 1)
    sc = (er * (fast_sc - slow_sc) + slow_sc) ** 2
    kama = prices.copy()
    for i in range(er_period, len(prices)):
        kama.iloc[i] = kama.iloc[i - 1] + sc.iloc[i] * (prices.iloc[i] - kama.iloc[i - 1])
    return kama

def calculate_roc(prices, period=14):
    return prices.pct_change(periods=period)

def calculate_atr(high, low, close, period=14):
    tr = pd.concat([
        high - low,
        (high - close.shift()).abs(),
        (low - close.shift()).abs()
    ], axis=1).max(axis=1)
    return tr.rolling(window=period).mean()

def calculate_di(high, low, close, period=14):
    plus_dm = high.diff()
    minus_dm = low.diff().abs()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm < 0] = 0
    tr = high.combine(low, max) - high.combine(low, min)
    tr[tr == 0] = 1e-10
    plus_di = 100 * (plus_dm.rolling(period).mean() / tr.rolling(period).mean())
    minus_di = 100 * (minus_dm.rolling(period).mean() / tr.rolling(period).mean())
    return plus_di, minus_di
