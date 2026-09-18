class Node:
  # Constructor to initialize the node with data and next pointer
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")
# Creating nodes for the linked list
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)
# Linking nodes to form the linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)