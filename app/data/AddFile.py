
import os


def CheckForRecursion(ticker):
    pass


def RetrieveData(file, depth):

    depthCounter = 0
    lines = []

    with open(file) as f:

        lines = f.readlines()

        # look through

    for line in lines:
        pass


def AddFile(ticker):
    pass


def AddData(FileName):
    pass


def CheckDataBase(ticker, depth):

    if os.path.exists(f'app/data/database/{ticker}.txt') is False:
        print("Making Data File")
    else:
        print("File Found, retrieving data")
        RetrieveData(f'app/data/database/{ticker}.txt', depth)
        # TODO Crawl through the file and return the data


if __name__ == '__main__':
    CheckDataBase('AAPL', 4)
