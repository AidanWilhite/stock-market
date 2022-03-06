
from audioop import reverse
import math
from statistics import mean

import numpy as np


LineData = [
    1.,
    0.
]

Accuracy = 0.
InterquartileRange = 0.
Mean = 0.


def SetLinearReg(x, y):

    global LineData

    En_x = 0.
    EnSq_x = 0.

    En_y = 0.

    SqEn_xy = 0.

    Slope = 0.

    DataP = 0

    lenY = len(y)
    lenX = len(x)

    # gets En_x and En_y
    for i in range(lenX):
        En_x += x[i]
        DataP += 1

        En_y += y[i]

        for j in range(lenX):
            SqEn_xy += i * j
            EnSq_x += i * j

    d = (DataP * SqEn_xy) - (En_x * En_y)
    n = (DataP * EnSq_x) - ((En_x) ** 2)

    Slope = (d/n)
    YIntercept = (En_y - (Slope * En_x)) / DataP

    LineData.clear()
    LineData.append(Slope)
    LineData.append(YIntercept)

    # Go through all points on predicted line and all points on real line and see how close they are

    R = 0.

    for Dy in range(lenY):
        R += abs(y[Dy] - GetReg(Dy))
        #print(abs(y[Dy] - GetReg(Dy)))

    global Accuracy
    global InterquartileRange
    global Mean

    InterquartileRange = FindInterRange(y)
    Accuracy = R / lenY
    Mean = mean(y)


def GetReg(y):
    # y = mx+b
    global LineData

    s = LineData[0]
    yi = LineData[1]

    #print(str((s * y) + yi))

    return float((s * y) + yi)


def FindInterRange(d):  # thanks to https://www.geeksforgeeks.org/interquartile-range-and-quartile-deviation-using-numpy-and-scipy/ for this

    Q1 = np.median(d[:10])

    Q3 = np.median(d[10:])

    IQR = abs(Q1 - Q3)

    return IQR


def GetAccuracy():
    return Accuracy


def GetInterRange():
    global InterquartileRange
    return float(InterquartileRange)


def GetMean():
    return Mean
