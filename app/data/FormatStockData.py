
#import pandas as pd
import yfinance as yf


def FormatStockDataToNum(Token, Depth):

    RawData = yf.Ticker(Token).history(period=str(Depth) + 'mo')

    PDat = RawData.get("Close")

    Data = PDat.to_numpy()

    return Data
