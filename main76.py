class Node():

    def __init__(self, value: int, next = None) -> None:
        self.value = value
        self.next = next

class LinkedList():

    def __init__(self, head = None) -> None:
        self.head = head
        self.pointer = None
        self.i = 0

    def add(self, value: int) -> None:

        if self.i == 0:
            self.head = Node(value)
            self.pointer = self.head
            self.i += 1
            return
        
        self.pointer.next = Node(value)

        self.pointer = self.pointer.next

        self.i += 1

    def partition(self, k: int) -> None:

        pointerHelper = self.head
        pointerHelper0 = self.head

        for i in range(self.i - 1):

            for j in range(self.i - 1):
                if pointerHelper.value >= k and pointerHelper.value > pointerHelper.next.value and pointerHelper.next.value < k:
                    pointerHelper.value, pointerHelper.next.value = pointerHelper.next.value, pointerHelper.value

                pointerHelper = pointerHelper.next

            pointerHelper = self.head
            pointerHelper0 = pointerHelper0.next

    def __str__(self) -> str:
        
        pointer = self.head
        result: str = ''

        for i in range(self.i):

            result += str(pointer.value)

            if pointer.next:
                result += ' -> '
            
            pointer = pointer.next

        return result

linkedList: LinkedList = LinkedList()

linkedList.add(5)
linkedList.add(1)
linkedList.add(8)
linkedList.add(0)
linkedList.add(3)

print(linkedList)

linkedList.partition(3)

print(linkedList)