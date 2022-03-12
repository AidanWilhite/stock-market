
import math
from app.Workers.LinRegWorkers import Work
from app.data import getData


if __name__ == "__main__":

    Stockdepth = 2
    ticker = "AAPL"

    StockData = getData(ticker, Stockdepth)

    X_DATA_LIST = []
    Y_DATA_LIST = [x for x in StockData if math.isnan(x) == False]

    Y_DATA_LIST.reverse

    for i in range(len(Y_DATA_LIST)):
        X_DATA_LIST.append(i)

    print(f'Answer : {Work(X_DATA_LIST, Y_DATA_LIST, Depth=Stockdepth)}')
    # Check wether we are accurate or not
    # only send data with one value missing from the end
