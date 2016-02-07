class Deque:
    def __init__(self):
        self.list = []

    def addFront(self, data):
        self.list.insert(0, data)

    def removeFront(self):
        self.list.pop(0)

    def addRear(self, data):
        self.list.append(data)

    def removeRear(self):
        self.list.pop(self.list[len(self.list) - 1])

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return len(self.list) == 0

    def getQueue(self):
        return self.list


d = Deque()
d.addFront(1)
d.addFront(2)
d.addRear(6)
d.addFront(5)
print d.getQueue()
