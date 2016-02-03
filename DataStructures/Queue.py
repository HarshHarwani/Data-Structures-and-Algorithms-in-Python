class Queue:
    def __init__(self):
        self.list = []

    def insert(self, data):
        self.list.append(data)

    def remove(self):
        if self.isEmpty():
            print "Queue is Empty"
            return None
        else:
            return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.list[0]

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return len(self.list) == 0

    def getQueue(self):
        return self.list


class Queue_a:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.size = 0
        self.list = []

    def insert(self, data):
        if (self.rear == -1):
            self.front += 1
        self.rear += 1
        self.list.insert(self.rear,data)
        self.size += 1

    def remove(self):
        if self.isEmpty():
            return
        else:
            ele = self.list[self.front]
            if (self.front == self.rear):
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            self.size -= 1
            return ele

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.list[self.front]

    def isEmpty(self):
        if (self.front == -1):
            print "Queue is empty"
            return True
        else:
            return False

    def get_size(self):
        return self.size

    def getQueue(self):
        for i in range(self.front,self.rear):
            print(self.list[i])
