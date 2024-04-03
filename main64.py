class Node():

    def __init__(self, value: int, next = None) -> None:

        self.value = value
        self.next = next
        self.pointer = None

    def __str__(self) -> str:

        result: str = ''

        self.pointer = linkedList.start

        for i in range(linkedList.i):

            result += str(self.pointer.value)

            if i < linkedList.i - 1:
                result += ' -> '

            self.pointer = self.pointer.next

        return result

class LinkedList():

    def __init__(self) -> None:

        self.start = None
        self.pointer = None
        self.i: int = 0
        self.pointerStart = None
        self.pointerEnd = None

    def add(self, value: int) -> None:

        if self.i == 0:
            self.start = Node(value)
            self.pointer = self.start
            self.i += 1
            return

        self.pointer.next = Node(value)

        self.pointer = self.pointer.next

        self.i += 1

    def reverse(self, k: int) -> None:

        self.pointerStart = self.start
        self.pointerEnd = self.start
        it: int = 0
        it0: int = 0

        for x in range(self.i):

            it = 0

            for y in range(self.i - it0):

                if it == k:

                    self.pointerStart.value, self.pointerEnd.value = self.pointerEnd.value, self.pointerStart.value
                    break

                self.pointerEnd = self.pointerEnd.next

                it += 1

            it0 += 1 

            self.pointerStart = self.pointerStart.next
            self.pointerEnd = self.pointerStart

        self.pointerStart = self.start

        it = 0
        it0 = 0
        it1: int = 1

        if k % 2 != 0 and self.i % k != 0:

            self.pointerStart = self.start
            self.pointerEnd = self.start

            for x in range(k):

                for y in range(k - it):

                    it0 += 1

                    if it0 == k - it1:

                        self.pointerStart.value, self.pointerEnd.value = self.pointerEnd.value, self.pointerStart.value

                        it0 = 0
                        it1 += 1

                    self.pointerEnd = self.pointerEnd.next

                self.pointerStart = self.pointerStart.next
                self.pointerEnd = self.pointerStart

                it += 1


linkedList: LinkedList = LinkedList()

linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)

linkedList.reverse(3)

print(linkedList.start)