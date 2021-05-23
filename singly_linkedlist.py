class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head 
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def insertAtBeg(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp

    def insertAtMid(self,newNode,pos):
        if self.head is None:
            self.head = newNode  

    
    def printList(self):
        currentNode = self.head
        while True:
            
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

 

firstNode=Node("geetanshu")
ll = LinkedList()
ll.insertAtEnd(firstNode)
secondNode = Node("naina")
ll.insertAtEnd(secondNode)
thirdNode = Node("simmi")
ll.insertAtBeg(thirdNode)
ll.printList()