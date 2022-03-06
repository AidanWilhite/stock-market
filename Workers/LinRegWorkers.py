
from concurrent.futures import thread
from re import L
import sys
import time
import threading

# TODO add tasks for the bot to do


class LinWorker():

    def __init__(self, XDat, YDat, FragCatch, Name):
        self.XDat = XDat  # x data to evaluate
        self.YDat = YDat  # y data to evaluate
        self.FragCatch = FragCatch  # what fragment of the data is this worker getting
        self.Name = Name  # what is their name?
        self.Working = False
        self.TotalTime = time.time()

    def BeginTask(self):

        self.Working = True
        Log = threading.Thread(target=self.LogProgress)
        Log.start()

        RetVal = self.Task()  # calcualte the return value

        self.Working = False
        self.TotalTime = time.time() - self.TotalTime

        print(" " * 50, end="\r")
        print(
            f"{self.Name} Completed Frag {self.FragCatch} in {self.TotalTime} ================ Answer : {RetVal}")

    def Task(self):
        return self.XDat + self.YDat

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
                    time.sleep(0.25)


class LinRegWork():

    def __init__(self, Workers):
        self.Workers = Workers

    def Start(self):

        for work in self.Workers:

            # waits for the current worker to return
            work.BeginTask()


if __name__ == "__main__":
    # AnimateLoadingbar("Loading")

    l = LinRegWork(Workers=[
        LinWorker(1, 2, 0, "Fred"),
        LinWorker(1, 1, 0, "Ted"),
        LinWorker(1, 3, 0, "Bill")
    ]
    )

    l.Start()
