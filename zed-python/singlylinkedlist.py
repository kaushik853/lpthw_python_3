#create node
#create Linkedlist
#add node to Linkedlist
#print Linkedlist
#head is the first linkedlist with data,next as None


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,newNode):
        # head => john => None
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newNode

    def printlist(self):
        # head => john -> ben -> mathew -> None
        if self.head is None:
            print("Empty list")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(f"the data is : {currentnode.data}")
            print(f"The next node is: {currentnode.next}")
            currentnode = currentnode.next



#Node => data,next
#firstnode.data => john,firstnode.next => None

firstnode = Node("john")
Singlelinkedlist = Linkedlist()
Singlelinkedlist.insert(firstnode)
secondnode = Node("ben")
Singlelinkedlist.insert(secondnode)
thirdnode = Node("mathew")
Singlelinkedlist.insert(thirdnode)
Singlelinkedlist.printlist()
