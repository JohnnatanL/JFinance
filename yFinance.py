import yfinance as yf
import pandas as pd

def hist(ticker):
    ticker = ticker+".SA"
    ticker = yf.Ticker(ticker)
    hist = ticker.history(period="1mo")
    df = pd.DataFrame(hist)
    df = df.sort_values(['Date'], ascending=False)
    return df