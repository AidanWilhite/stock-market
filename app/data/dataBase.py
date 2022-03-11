
from datetime import datetime
import os
from time import time
import numpy

import yfinance


def RenewDataBase():
    # TODO Add to the file
    # we could rewrite the whole file
    pass


def RetrieveData(file, depth, ticker):

    depthCounter = 0
    lines = []
    SelectedData = []

    with open(file) as f:
        lines = f.readlines()

    lines[0].strip()

    t = str(lines[0].strip())
    ct = str(datetime.today().strftime("%B %d, %Y").strip())

    if t != ct:
        print("Rewriting Database")
        with open(f'app/data/database/{ticker}.txt', 'r+') as f:
            data = yfinance.Ticker(ticker).history(
                period='32mo').get("Close").to_numpy()
            content = numpy.flipud(data)[0]
            line = datetime.today().strftime("%B %d, %Y").strip()

            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + str(content))

    for line in lines:
        if line[0] == ":" and int(line[1]) == depth:
            return SelectedData
        else:
            if line[0] != ":" and line[0] != "=" and line != lines[0]:
                SelectedData.append(float(line))


def AddFile(ticker):
    with open(f'app/data/database/{ticker}.txt', 'w') as f:
        Data = (yfinance.Ticker(ticker).history(
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
        return RetrieveData(f'app/data/database/{ticker}.txt', depth, ticker)


if __name__ == '__main__':
    CheckDataBase('AAPL', 3)
