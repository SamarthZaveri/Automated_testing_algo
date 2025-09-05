def compute_rsi(series, window=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


# Moving Average Crossover + RSI logic
def generate_signals(df):
    df['RSI'] = compute_rsi(df['Close'])
    df['20DMA'] = df['Close'].rolling(window=20).mean()
    df['50DMA'] = df['Close'].rolling(window=50).mean()


    df['Signal'] = "HOLD"
    df.loc[(df['RSI'] < 30) & (df['20DMA'] > df['50DMA']), 'Signal'] = "BUY"
    df.loc[(df['RSI'] > 70) & (df['20DMA'] < df['50DMA']), 'Signal'] = "SELL"
    return df