
import sys
import time
import threading

from app.calc.EvaluateWork import evalWork

from ..calc.LinReg import SetLinearReg, GetReg

# TODO add tasks for the bot to do


class LinWorker():

    def __init__(self, XDat, YDat, FragCatch, Name, pX):
        self.XDat = XDat  # x data to evaluate
        self.YDat = YDat  # y data to evaluate
        self.FragCatch = FragCatch  # what fragment of the data is this worker getting
        self.Name = Name  # what is their name?
        self.Working = False
        self.TotalTime = 0
        self.LinDataCache = [0, 0, 0, 0, 0]
        self.sol = 0
        self.SolCache = []
        self.Px = pX

    def BeginTask(self):

        self.Working = True
        self.TotalTime = time.time()
        Log = threading.Thread(target=self.LogProgress)
        Log.start()

        RetVal = self.Task()  # calcualte the return value

        self.Working = False
        self.TotalTime = time.time() - self.TotalTime
        self.sol = RetVal

        print(" " * 50, end="\r")
        print(
            f"{self.Name} Completed Frag {self.FragCatch} in {self.TotalTime} ================ Answer : {RetVal}")

    def Task(self):

        # self.LinDataCache =
        lin = SetLinearReg(self.XDat, self.YDat)
        self.SolCache = lin
        return GetReg(self.Px + 1, lin)

    def LogProgress(self):

        AnimationFrames = [
            "/",
            "-",
            "\\",
            "|"
        ]

        while self.Working is True:
            for f in AnimationFrames:
                if self.Working is False:
                    break
                else:
                    sys.stdout.write(
                        f'\r{self.Name} Finding Frag {self.FragCatch} ' + f)
                    sys.stdout.flush()
                    time.sleep(0.1)


class LinRegWork():

    def __init__(self, Workers):
        self.Workers = Workers

    def Start(self):

        for work in self.Workers:

            work.BeginTask()


def Work(x, y, Depth):

    # TODO Split the data between 2 bots patric and Zoe and have them complete 2 diffrant modles of lin reg and compare them

    Full = len(x)
    Mid = round(len(x) / 2)
    mm = round(Mid/2)
    mmm = round(mm/2)

    l = LinRegWork(Workers=[
        LinWorker(x[0:mmm], y[0:mmm], 1.125, "1/8", Full),
        LinWorker(x[mmm:mm], y[mmm:mm], 1.25, "2/8", Full),
        LinWorker(x[mm:mm + mmm], y[mm:mm + mmm], 1.375, "3/4", Full),
        LinWorker(x[mm + mmm:Mid], y[mm + mmm:Mid], 1.5, "4/8", Full),
        LinWorker(x[Mid:Mid + mmm], y[Mid:Mid + mmm], 1.625, "5/8", Full),
        LinWorker(x[Mid:mmm+Mid], y[Mid:mmm+Mid], 1.75, "6/8", Full),
        LinWorker(x[mmm+Mid:mmm+Mid+mm],
                  y[mmm+Mid:mmm+Mid+mm], 1.75, "7/8", Full),
        LinWorker(x[mmm+mm+Mid:Full], y[mmm+mm+Mid:Full], 1.4, "4/4", Full),
        LinWorker(x, y, 2, "Full", Full),
    ]
    )

    l.Start()

    return evalWork(l)


# just in case i want to test from here to see if things are working proporly
