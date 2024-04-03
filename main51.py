import heapq

class Stack():

    def __init__(self) -> None:

        self.content: list = []
        self.it: int = 0

    def push(self, item: int) -> None:
        
        #self.content.append(item)

        heapq.heappush(self.content, item)

    def pop(self) -> int:
        
        return heapq.heappop(self.content)
    
stack: Stack = Stack()

stack.push(5)
stack.push(4)
stack.push(3)

print(stack.content)

print(stack.pop())
print(stack.pop())
print(stack.pop())