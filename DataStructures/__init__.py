from DataStructures.LinkedList import LinkedList
from DataStructures.Stack import Stack
from DataStructures.Queue import Queue

##==========================================LinkedList======================================##
list = LinkedList()
list.insert(1)
list.insert_end(2)
list.insert_end(3)
list.insert_end(4)
list.insert_end(5)
list.insert_end(6)
list.remove_data(10)
print "list is-->"
list.printList()
print "The size of the list is-->", list.size
##==========================================Stack======================================##

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


##==========================================Queue======================================##
q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
print "The removed element is",q.remove()
print "The removed element is",q.remove()
q.insert(5)
print "The top element is",q.peek()
print "The size of the queue is",q.size()
print "Whether queue is empty? :",q.isEmpty()
print "The queue is",q.getQueue()