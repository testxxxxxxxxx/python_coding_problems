def reverse(lst: list, i: int, j: int) -> list:

    startList: list = lst[0:i]
    tempList: list = lst[i:j]
    endList: list = lst[j:]
    revArr: list = []

    for i in range(len(tempList)):

        revArr.append(tempList[len(tempList) - 1 - i])
        
    lst = startList + revArr + endList

    return lst

def sort(lst: list) -> list:

    for i in range(len(lst)):

        for j in range(len(lst) - 1 - i):

            if lst[j] > lst[j + 1]:

                lst = reverse(lst, j, j + 2)

    return lst

lst: list = [6, 3, 4, 5]

lst = sort(lst)

print(lst)