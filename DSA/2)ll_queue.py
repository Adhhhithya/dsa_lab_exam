class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.ctr = 0

    def Enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        print("Node enqueued to queue:", data)
        self.ctr += 1

    def Dequeue(self):
        if self.front is None:
            print("No Nodes exist")
        else:
            print("Dequeued from queue:", self.front.data)
            self.front = self.front.next
            self.ctr -= 1

    def Traverse(self):
        if self.front is None:
            print("No Nodes exist")
            return
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next

def Menu():
    print("1.Enqueue\n2.Dequeue\n3.Traverse\n4.Number of nodes\n5.Exit")
    ch = int(input("Enter choice: "))
    return ch

# Main program
print("******************* Queue *************")
s = Queue()
while True:
    ch = Menu()
    if ch == 1:
        data = input("Enter data: ")
        s.Enqueue(data)
    elif ch == 2:
        s.Dequeue()
    elif ch == 3:
        s.Traverse()
    elif ch == 4:
        print("Number of nodes:", s.ctr)
    else:
        print("Quit")
        break
