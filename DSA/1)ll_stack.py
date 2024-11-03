class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.ctr = 0
        self.top = None

    def Push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.top = node
        else:
            self.top.next = node
            self.top = node
        print("Node pushed to stack:", data)
        self.ctr += 1

    def Pop(self):
        if self.head is None:
            print("Stack Underflow")
        elif self.head == self.top:
            print("Deleted from Stack:", self.head.data)
            self.head = self.top = None
            self.ctr -= 1
        else:
            print("Deleted from Stack:", self.top.data)
            temp = self.head
            while temp.next is not self.top:
                temp = temp.next
            temp.next = None
            self.top = temp
            self.ctr -= 1

    def Traverse(self):
        if self.head is None:
            print("No Nodes exist")
            return
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

def Menu():
    print("1.Push\n2.Pop\n3.Traverse\n4.Number of nodes\n5.Exit")
    ch = int(input("Enter choice: "))
    return ch

# Main program
s = Stack()
print("****** Stack ******")
while True:
    ch = Menu()
    if ch == 1:
        data = input("Enter data: ")
        s.Push(data)
    elif ch == 2:
        s.Pop()
    elif ch == 3:
        s.Traverse()
    elif ch == 4:
        print("Number of nodes:", s.ctr)
    else:
        print('Quit')
        break
