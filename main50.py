class Node():

    def __init__(self, value: int = 0, left = None, right = None) -> None:

        self.value = value
        self.left = left
        self.right = right

class Heap():

    def __init__(self) -> None:
        self.start: Node = Node()
        self.i: int = -1
        self.pointerLeft: Node = Node()
        self.pointerRight: Node = Node()
        self.state: int = 0
        self.state0: int = 0
        self.state1: bool = False
        self.subTree: Node = Node()
        self.pointer: Node = self.subTree
        self.finalPointer: Node = Node()
        self.it: int = 0

    def push(self, value: int) -> None:

        def getSubTree() -> None:
            
            if self.i == 3:

                self.i = 0

            if self.i == 0:

                self.pointer.value = value

                self.pointer.left = Node()

                self.pointer.right = Node()

                self.pointerLeft = self.pointer.left

                self.pointerRight = self.pointer.right

                self.i += 1

                self.subTree = self.pointer

                return 
        
            if self.state == 0:

                self.pointerLeft.value = value

                self.state = 1

            elif self.state == 1:

                self.pointerRight.value = value

                self.state = 0

            self.subTree = self.pointer

            self.i += 1

            return 
        
        getSubTree()
        
        if self.it <=3:

            self.start = self.subTree

            self.finalPointer = self.start

            self.it += 1
            return

        if not self.state1 and self.it%3 != 0:

            self.finalPointer.left.left = self.subTree

        elif self.state1 == 1 and self.it%3 != 0:

            self.finalPointer.right.right = self.subTree

        if self.it > 3 and self.it%3 == 0:

            if not self.state1:

                self.finalPointer = self.finalPointer.left.left

            else:
                self.finalPointer = self.finalPointer.right.right

            self.state1 = not self.state1 

            self.subTree = Node()

        self.it += 1

    def push0(self, item: int) -> None:

        self.i += 1

        if self.i == 0:

            self.pointer = self.start

            self.start.value = item

            self.pointerLeft = self.start
            self.pointerRight = self.start

            return

        if self.state == 0:

            self.pointerLeft.left = Node(item)

            self.pointerLeft = self.pointerLeft.left

            self.state = 1
            return
        else:
            self.pointerRight.right = Node(item)

            self.pointerRight = self.pointerRight.right

            self.state = 0
            return



class Stack():

    def __init__(self) -> None:
        self.heap = None
        self.pointer = None

    def push(self, item: int) -> None:
        pass

heap: Heap = Heap()

heap.push0(1)
heap.push0(2)
heap.push0(3)
heap.push0(4)
heap.push0(5)
heap.push0(6)

print(heap.start.value)