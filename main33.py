def solution(intervals: list) -> set:

    intervals.sort()

    start: int = intervals[0][1]
    end: int = start
    intervalStart: int = 0
    intervalEnd: int = 0
    pos: int = 1

    for i in intervals[1:]:

        intervalStart, intervalEnd = i

        if start > intervalStart and start > intervalEnd:
            start = intervalEnd
            pos += 1
        else:
            break

    for j in intervals[pos:]:

        intervalStart, _ = j

        if intervalStart > end:
            end = intervalStart


    return set({start, end})
        
print(solution([[0, 3], [2, 6], [3, 4], [6, 9]]))