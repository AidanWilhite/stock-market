
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
        # TODO look through data until we find :# and log the number we find inside
        if line[0] == ":" and int(line[1]) == depth:
            print(SelectedData)
            break
        else:
            if line[0] != ":" and line[0] != "=":
                print(line)
                SelectedData.append(line)


def AddFile(ticker):
    with open(f'app/data/database/{ticker}.txt', 'w') as f:
        # TODO get yahoo finance to write some data to this file and we are good to go!
        Data = (yfinance.Ticker("AAPL").history(
            period='32mo')).get("Close").to_numpy()

        Data = numpy.flipud(Data)

        for i in Data:
            f.write(f'{i}\n')


def AddData(FileName):
    pass


def CheckDataBase(ticker, depth):

    if os.path.exists(f'app/data/database/{ticker}.txt') is False:
        print("Making Data File")
        AddFile(ticker)
    else:
        print("File Found, retrieving data")
        RetrieveData(f'app/data/database/{ticker}.txt', depth)


if __name__ == '__main__':
    CheckDataBase('AAPL', 4)
