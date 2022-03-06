
import sys
import time
import threading

from ..calc.LinReg import SetLinearReg, GetReg

# TODO add tasks for the bot to do


class LinWorker():

    def __init__(self, XDat, YDat, FragCatch, Name):
        self.XDat = XDat  # x data to evaluate
        self.YDat = YDat  # y data to evaluate
        self.FragCatch = FragCatch  # what fragment of the data is this worker getting
        self.Name = Name  # what is their name?
        self.Working = False
        self.TotalTime = 0
        self.LinDataCache = [0, 0, 0, 0, 0]

    def BeginTask(self):

        self.Working = True
        self.TotalTime = time.time()
        Log = threading.Thread(target=self.LogProgress)
        Log.start()

        RetVal = self.Task()  # calcualte the return value

        self.Working = False
        self.TotalTime = time.time() - self.TotalTime

        print(" " * 50, end="\r")
        print(
            f"{self.Name} Completed Frag {self.FragCatch} in {self.TotalTime} ================ Answer : {RetVal}")

    def Task(self):

        # self.LinDataCache =
        return GetReg(len(self.XDat) + 1, SetLinearReg(self.XDat, self.YDat))

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

    l = LinRegWork(Workers=[
        LinWorker(x, y, 0, "Patric"),
    ]
    )

    l.Start()


# just in case i want to test from here to see if things are working proporly
