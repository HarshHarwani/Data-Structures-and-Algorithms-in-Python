class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def insert_end(self,data):
        current=self.head
        while current.get_next():
            current=current.get_next()
        new_node=Node(data)
        current.set_next(new_node)

    def insert_index(self,data,index):
        if index < 0 or index > self.size:
            raise ValueError("Index is inValid")
        elif index==0:
            self.insert(data)
        else:
            current=self.head
            for i in range(0,index):
                current=current.get_next()
            next=current.get_next()
            new_node=Node(data)
            current.set_next(new_node)
            new_node.set_next(next)

    def get_size(self):
        return self.size

    def remove_data(self, data):
        #**this method does not work when the node to be deleted is last
        node_to_be_deleted=self.find(data)
        next=node_to_be_deleted.get_next()
        node_to_be_deleted.set_data(next.get_data())
        node_to_be_deleted.set_next(next.get_next())
        return

    def find(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current.get_data()
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data is not in list")
        return current.get_data()

    def printList(self):
        current=self.head
        while current:
            print str(current.get_data())
            current=current.get_next()


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data=data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



list=LinkedList()
list.insert(1)
list.insert_end(2)
list.insert_end(3)
list.insert_end(4)
list.insert_end(5)
list.insert_end(6)
list.printList()

