class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            print "Empty Stack"
            return None
        else:
            return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

s=Stack()
s.push("Harsh")
s.push(1)
s.push("2")
print s.pop()
print s.peek()
print s.pop()
print s.pop()
print s.pop()
print s.size()
print s.isEmpty()