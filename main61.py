def solution(entriesAndExists: list) -> tuple:

    maxCount: int = 0
    count: int = 0
    start: int = entriesAndExists[0]["timestamp"]
    maxStart: int = 0
    maxEnd: int = 0
    end: int = 0

    for i in range(len(entriesAndExists) - 1):

        if entriesAndExists[i]["type"] == 'enter':
            count += entriesAndExists[i]["count"]

        elif entriesAndExists[i]["type"] == 'exit':
            if count > 0:
                count -= entriesAndExists[i]["count"]

            if count < 0:
                count = 0

        if count == 0:
             start = entriesAndExists[i + 1]["timestamp"]

        end = entriesAndExists[i]["timestamp"]

        if count > maxCount:
                
                if entriesAndExists[i + 1]["type"] == 'enter':
                     count += entriesAndExists[i + 1]["count"]
                     end = entriesAndExists[i + 1]["timestamp"] 

                maxCount = count
                maxStart = start
                maxEnd = end
                count = 0

    return (maxStart, maxEnd)

entriesAndExists: list = [

    {"timestamp": 1526579928, "count": 3, "type": "enter"},
    {"timestamp": 1526580382, "count": 2, "type": "exit"},
    {"timestamp": 1708793825, "count": 2, "type": "enter"},
    {"timestamp": 1708797425, "count": 4, "type": "enter"},
    {"timestamp": 1708801026, "count": 3, "type": "enter"},
    {"timestamp": 1708804629, "count": 3, "type": "exit"},
    {"timestamp": 1708804670, "count": 3, "type": "enter"},
    {"timestamp": 1708804680, "count": 12, "type": "enter"},
    {"timestamp": 1708804690, "count": 3, "type": "exit"},
    {"timestamp": 1708804695, "count": 4, "type": "exit"},
    {"timestamp": 1708804700, "count": 10, "type": "enter"},
    {"timestamp": 1708804710, "count": 3, "type": "enter"},
    {"timestamp": 1708804715, "count": 3, "type": "exit"},
    {"timestamp": 1708804720, "count": 30, "type": "enter"},
    {"timestamp": 1708804721, "count": 31, "type": "enter"}

]

print(solution(entriesAndExists))