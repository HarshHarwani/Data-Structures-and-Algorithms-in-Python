from DataStructures.Queue import Queue
import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm;
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def isBusy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNewTask(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, timeStamp):
        self.timeStamp = timeStamp
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages

    def waitingTime(self, currentTime):
        return currentTime - self.timeStamp


def newTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, PPM):
    printer = Printer(PPM)
    queue = Queue()
    waitingTime = []

    for currentTime in range(numSeconds):
        if newTask():
            queue.insert(Task(currentTime))

        if (not printer.isBusy()) and (not queue.isEmpty()):
            nextTask = queue.remove()
            waitingTime.append(nextTask.waitingTime(currentTime))
            printer.startNewTask(nextTask)

        printer.tick()
    averageWait = sum(waitingTime) / len(waitingTime)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, queue.size()))


for i in range(10):
    simulation(3600, 5)
