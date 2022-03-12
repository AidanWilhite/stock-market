
import cProfile
import math
from re import I
from tkinter import Y, Canvas, Tk
from app.Workers.LinRegWorkers import Work
from app.calc import LinReg
import app.calc.LinReg
from app.data import getData


def create_circle(x, y, r, canvasName, color):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill=color)


def MakeGraph(Dat_x, Dat_y, XHigh, YHigh):

    root = Tk()
    root.geometry("800x800")

    ScaleX = 600 / (XHigh)
    ScaleY = 600 / (YHigh)

    c = Canvas(root, height=800, width=800)

    for i in range(len(Dat_y)):

        create_circle((Dat_y[i] * ScaleY) + 100,
                      (Dat_x[i] * ScaleX) - 200, 2, c, "black")

        if (LinReg.GetInterRange() * 1.5) + LinReg.GetMean() > Dat_x[i] and (LinReg.GetInterRange() * -1.5) + LinReg.GetMean() < Dat_x[i]:

            create_circle((Dat_y[i] * ScaleY) + 100,
                          (LinReg.GetReg(i) * ScaleX) - 200, 2, c, "red")

    c.pack()

    root.mainloop()


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
