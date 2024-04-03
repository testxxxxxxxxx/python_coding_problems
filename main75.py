def sort(arr: list) -> None:

    for i in range(len(arr)):

        for j in range(1 ,len(arr) - i):

            if arr[j - 1][0] > arr[j][0]:

                arr[j - 1], arr[j] = arr[j], arr[j - 1]

def color(graph: list) -> bool:

    sort(graph)

    keys: list = [i for i in graph]
    values: list = ['N' for i in graph]
    color: int = 0
    select: int = 0

    for x in range(len(graph)):

        color = 0

        for i in range(len(graph)):

            select = graph[x][0]

            color = 0

            for j in range(len(graph)):

                if graph[j][0] == select and values[keys.index(graph[j])] == 'N':

                    select = graph[j][1]

                    values[keys.index(graph[j])] = color

                    if color == 0:
                        color = 1
                    else:
                        color = 0

        if graph[x][0] != 0 or graph[x][1] != 0:
            break


    for i in range(1, len(graph)):

        if keys[i - 1][0] == keys[i][0] and values[i] == 'N':

            values[i] = values[i - 1]

    for i in range(len(graph)):

        select = keys[i][1]
        lastColor: int = values[keys.index(keys[i])]

        for j in range(len(graph)):

            if graph[j][0] == select and i != j:

                select = graph[j][1]

                if lastColor == values[keys.index(keys[j])]:
                    return False
                
                lastColor = values[keys.index(keys[j])]


    return True

print(color([(0, 1), (0, 3) ,(1, 2), (2, 3), (2, 5), (3, 4), (4, 5)]))