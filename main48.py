class Stack():

    def __init__(self) -> None:

        self.content: list = []
        self.heap: int = -1

    def push(self, item: int) -> None:

        self.content.append(item)
        self.heap += 1

    def pop(self) -> int:

        item: int = self.content[self.heap]

        self.content.pop(self.heap)

        self.heap -= 1

        return item
    
stack: Stack = Stack()

stack.push(5)
stack.push(4)
stack.push(3)

print(stack.pop())
print(stack.pop())