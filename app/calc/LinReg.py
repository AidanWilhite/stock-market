
from functools import cache
from statistics import mean
import warnings

import numpy as np


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

    Results = []

    # gets En_x and En_y
    for i in range(lenX):
        En_x += x[i]
        DataP += 1

        En_y += y[i]

        # for j in range(lenY):
        SqEn_xy += x[i] * y[i]
        EnSq_x += x[i] ** 2

    d = (SqEn_xy) - ((En_x * En_y) / DataP)
    n = (EnSq_x) - (((En_x) ** 2) / DataP)
    # Go through all points on predicted line and all points on real line and see how close they are

    Results.append((d/n))
    Results.append((En_y - (Results[0] * En_x)) / DataP)

    R = 0.

    for Dy in range(lenY):
        R += abs(y[Dy] - GetReg(Dy, Results))
        #print(abs(y[Dy] - GetReg(Dy)))

    Results.append(FindInterRange(y))
    Results.append(lenY)
    Results.append(mean(y))

    return Results


def GetReg(y, CurrentData):

    # Brocken :(

    s = CurrentData[0]
    yi = CurrentData[1]

    #print(str((s * y) + yi))

    return float((s * y) + yi)


def FindInterRange(d):  # thanks to https://www.geeksforgeeks.org/interquartile-range-and-quartile-deviation-using-numpy-and-scipy/ for this
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)

        half = round(len(d)/2)

        Q1 = np.median(d[:half])

        Q3 = np.median(d[half:])

        IQR = abs(Q1 - Q3)

    return IQR
