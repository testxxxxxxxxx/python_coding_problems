class Node():

    def __init__(self, value: int, next = None) -> None:

        self.value = value
        self.next = next
        
class Stack():

    def __init__(self, start = None) -> None:

        self.start = start
        self.heap = self.start
        self.pointerRev = None
        self.it: int = 0

    def push(self, item: int) -> None:

        if self.it == 0:

            self.start = Node(item)
            self.heap = self.start
            self.it += 1

            return

        self.heap.next = Node(item)

        self.heap = self.heap.next

        self.it += 1        

    def pop(self) -> int:

        item: int = self.heap.value

        self.heap = self.start

        for i in range(self.it):

            if not self.heap.next:
                break

            if self.heap.next.next == None:
                self.heap.next = None
                break            

            self.heap = self.heap.next

        self.it -= 1

        return item
    
stack: Stack = Stack()

stack.push(5)
stack.push(4)
stack.push(3)

print(stack.pop())
print(stack.pop())