import imp


import yfinance
import numpy


def getData(ticker, depth):
    Data = (yfinance.Ticker(ticker).history(
            period=f'{depth}mo')).get("Close").to_numpy()

    return Data
