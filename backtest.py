import pandas as pd


def backtest(df, initial_capital=100000):
    capital = initial_capital
    position = 0
    trades = []


    for i in range(len(df)):
        if df['Signal'].iloc[i] == 'BUY' and position == 0:
            position = capital / df['Close'].iloc[i]
            capital = 0
            trades.append((df.index[i], 'BUY', df['Close'].iloc[i]))
        elif df['Signal'].iloc[i] == 'SELL' and position > 0:
            capital = position * df['Close'].iloc[i]
            position = 0
            trades.append((df.index[i], 'SELL', df['Close'].iloc[i]))


    final_value = capital + position * df['Close'].iloc[-1]
    return trades, final_value