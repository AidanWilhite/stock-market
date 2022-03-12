import imp
import sys


import yfinance
import numpy


def getData(ticker, depth):
    print('Getting Data')

    tick = yfinance.Ticker(ticker)

    Data = (tick.history(
            period=f'{depth}mo')).get("Close").to_numpy()

    if (len(Data) == 0):
        print(f"ticker {ticker} is invalid, please enter a real ticker")
        sys.exit()

    return Data
