class Queue:
    def __init__(self):
        self.list = []

    def insert(self, data):
        self.list.append(data)

    def remove(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return len(self.list) == 0

    def getQueue(self):
        return self.list


