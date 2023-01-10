# Creating a singly linked list
class Node:
    def __init__(self, value=None):
        self.value = value              #Set node value to the value passed
        self.next = None                #Set next node to the value passed

class SLinkedList:
    def __init__(self):                 #Initialize the function
        self.head = None                #Set head node to none
        self.tail = None                #Set tail node to none

    # Insertion method in Singly Linked List


    def insertSLL(self, value,location):
        newNode = Node(value)
        if self.head is None:           #Check if linkedlist is empty then make the node the head
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:               #Check if the newNode is to be inserted as the head
                newNode.next = self.head
                self.head = newNode
            elif location == -1:            #Check if the newNode should be inserted as the tail
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head         #Check if the newNode is to be inserted in any position other than head or tail
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

singlyLinkedList = SLinkedList()
node1 = Node(1)                         #Initialize the first node
node2 = Node(2)                         #Initialize a second node

singlyLinkedList.head = node1           #First node passed should be head
singlyLinkedList.head.next = node2      #Second node passed should the next node after head
singlyLinkedList.tail = node2           #Set second node to be the tail

#Every line of code here takes O(1) time complexity hence Time Complexity for creation = O(1)
#Space Complexity is O(1) but if we create more than 1 node, Space complexity is O(N)
