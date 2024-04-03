class Node():

    def __init__(self, value: str, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

class Tree():

    def __init__(self, dir: str, left = None, right = None) -> None:
        self.dir = dir
        self.left = left
        self.right = right
        self.listSt: list = self.dir.split("\n")
        self.s = iter(self.dir.split("\n"))
        self.it: int = 2 
    
    def addNode(self) -> Node:

        element = next(self.s)

        node = Node(element)

        node.left = self.addNode()
        node.right = self.addNode()

        return node            


tree = Tree("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")

def solution(dir: str) -> int:

    listSt: list = dir.split("\n")
    max_length: int = 0
    count: int = 0
    currentStrOld: str = ""
    currentStr: str = ""
    nextStrOld: str = ""
    nextStr: str = ""
    it: int = 0
    it0: int = 0

    for _ in range(len(listSt)):
        currentStrOld = str(listSt[it - 1]).replace("\t\t", "")
        currentStr = currentStrOld.replace("\t", "")
        nextStrOld = str(listSt[it]).replace("\t\t","")
        nextStr = nextStrOld.replace("\t", "")

        print(currentStr)

        for _ in range(len(currentStr)):
            count += 1

            if it0 == len(currentStr) - 1:
                it0 = 0

            if currentStr.find("subsub") != -1 and nextStr.find(".") == -1:
                count = 0

            if currentStr[it0] == ".":
                if count > max_length:
                    max_length = count
                    count = 0
            it0 += 1

        it += 1

    return max_length

print(solution("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))