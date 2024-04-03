from abc import ABC, abstractmethod

class Test_0(ABC):

    @abstractmethod
    def getX():
        pass
    @abstractmethod
    def getY():
        pass

class Test_1(Test_0):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    @property
    def getX(self)->int:
        return self.x
    def getY(self)->int:
        return self.y

test_1 = Test_1(5,4)

print(test_1.getX)
print(test_1.getY())