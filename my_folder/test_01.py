import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import pandas_datareader as web

pd.set_option('display.max_rows', None)


def calculate_ema(prices, days, smoothing=2):
    ema = [sum(prices[:days]) / days]
    for price in prices[days:]:
        ema.append((price * (smoothing / (1 + days))) +
                   ema[-1] * (1 - (smoothing / (1 + days))))
    return ema


symbol = 'MSFT'
df = web.DataReader(symbol, 'yahoo', '2015-01-01', '2016-01-01')

ema = calculate_ema(df['Close'], 10)

t = ema
df2 = pd.DataFrame([t]).T
me = df2.iloc[-1]
print(df2)
print(f'last {me}')
