
from datetime import datetime
import os
from time import time
import numpy

import yfinance


def RenewDataBase():
    # TODO Add to the file
    # we could rewrite the whole file
    pass


def RetrieveData(file, depth):

    depthCounter = 0
    lines = []
    SelectedData = []

    with open(file) as f:
        lines = f.readlines()

    lines[0].strip()

    # look through
#'March 09, 2022\n' 'March 09, 2022\n'
    # TODO check if the data needs to be renewed

    t = str(lines[0].strip())
    ct = str(datetime.today().strftime("%B %d, %Y").strip())

    if t != ct:
        print(t + " : " + ct)
        print("Renewing Database")

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

        f.write(f'={datetime.today().strftime("%B %d, %Y")}')

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
        print("Storing Data In New File")
        AddFile(ticker)
        return RetrieveData(f'app/data/database/{ticker}.txt', depth)
    else:
        print(f"{ticker} Found In Database, retrieving data")
        return RetrieveData(f'app/data/database/{ticker}.txt', depth)


if __name__ == '__main__':
    CheckDataBase('AAPL', 3)