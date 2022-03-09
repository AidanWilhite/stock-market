
import os
import numpy

import yfinance

#from app.data.FormatStockData import FormatStockDataToNum


def CheckForRecursion(ticker):
    pass


def RetrieveData(file, depth):

    depthCounter = 0
    lines = []
    SelectedData = []

    with open(file) as f:

        lines = f.readlines()

        # look through

    for line in lines:
        if line[0] == ":" and int(line[1]) == depth:
            return SelectedData
        else:
            if line[0] != ":" and line[0] != "=":
                SelectedData.append(float(line))


def AddFile(ticker):
    with open(f'app/data/database/{ticker}.txt', 'w') as f:
        Data = (yfinance.Ticker("AAPL").history(
            period='32mo')).get("Close").to_numpy()

        Data = numpy.flipud(Data)

        l = 0
        bench = round(len(Data) / 32)
        point = bench
        MonInc = 1

        for i in Data:
            if l == point:
                f.write(f':{MonInc}\n')
                MonInc += 1
                point += bench
            else:
                f.write(f'{i}\n')
                l = l+1


def CheckDataBase(ticker, depth):

    if os.path.exists(f'app/data/database/{ticker}.txt') is False:
        print("Making Data File")
        AddFile(ticker)
        print("Getting Data")
        return RetrieveData(f'app/data/database/{ticker}.txt', depth)
    else:
        print("File Found, retrieving data")
        return RetrieveData(f'app/data/database/{ticker}.txt', depth)
