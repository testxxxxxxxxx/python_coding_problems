class Node():

    def __init__(self, val) -> None:
        self.val = val
        self.both = 0

    def __str__(self):
        return str(self.val)
    
class XORLinkedList():
    def __init__(self) -> None:
        self.head = Node(None)
        self.tail = Node(None)
    
    def add(self, element):
        newNode: Node = Node(element)

        if self.head.val == None:
            self.head = self.tail = newNode
        else:
            newNode.both = get_pointer(self.tail)
            self.tail.both = self.tail.both ^ get_pointer(newNode)
            self.tail = newNode

    def get(self, index):
        previousAddr = 0
        current = self.head
        for i in range(0, index -1):
            temp = get_pointer(current)
            current = deference_pointer(previousAddr ^ current.both)
            previousAddr = temp
            if current.both == previousAddr and i < index - 2:
                print("Invalid index.")
                return None
        return current