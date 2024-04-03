def getLastElement(arr: list):

    for i in range(len(arr) - 1, -1, -1):

        return arr[i]
    
def removeLastElement(arr: list) -> None:

    for i in range(len(arr) - 1, -1, -1):

        arr.pop(i)
        return

def compute(numbers: list) -> int:

    resultStr: str = ''
    result: int = 0
    numbers0: list = []

    operands: list = [] 

    a: list = []

    for i in range(len(numbers)):

        if numbers[i] == '+' or numbers[i] == '-' or numbers[i] == '*' or numbers[i] == '/':
            operands.append(numbers[i])
        else:
            numbers0.append(numbers[i])

    for i in range(len(numbers0)):

        a.append(numbers0[i])
        a.append(getLastElement(operands))
        removeLastElement(operands)

    for x in range(len(numbers0) - 1, -1, -1):

        if numbers0[x] != None:
            result = numbers0[x]
            break

    print(a)

    for j in range(len(a) - 2, -1, -1):

        if a[j] == '+':
            result = a[j - 1] + result
        if a[j] == '-':
            result = a[j - 1] - result
        if a[j] == '*':
            result = a[j - 1] * result
        if a[j] == '/':
            result = a[j - 1] // result

    return result

print(compute([3, 15, 7, 1, 1, '+', '-', '/', '*']))