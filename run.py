
import argparse
import math
import sys
from app.Workers.LinRegWorkers import Work
from app.data import getData


def mainCLI():

    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        print('For help use -h')
        sys.exit()

    if len(sys.argv) < 2:
        print('You have specified too little arguments')
        print('For help use -h')
        sys.exit()

    my_parser = argparse.ArgumentParser(
        description='List the content of a folder')

    # Add the arguments
    my_parser.add_argument('Ticker',
                           metavar='path',
                           type=str,
                           help='The ticker of the stock you want to anylaze')

    my_parser.add_argument('Depth',
                           metavar='Depth',
                           type=str,
                           help='How far back you want to look')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    tick = args.Ticker
    depth = int(args.Depth)

    main(tick, depth, True)


def main(Usticker, depth, CLI):

    Stockdepth = 4
    ticker = 0

    if CLI is True:
        ticker = Usticker
        Stockdepth = depth
    else:
        ticker = input('Please enter a stock TICKER : ')
        Stockdepth = input('Please enter a depth, I recommend 2 : ')

    StockData = getData(ticker, Stockdepth)

    X_DATA_LIST = []
    Y_DATA_LIST = [x for x in StockData if math.isnan(x) == False]

    Y_DATA_LIST.reverse

    for i in range(len(Y_DATA_LIST)):
        X_DATA_LIST.append(i)

    print(f'Answer : {Work(X_DATA_LIST, Y_DATA_LIST, Depth=Stockdepth)}')


if __name__ == "__main__":
    mainCLI()

    # Check wether we are accurate or not
    # only send data with one value missing from the end
