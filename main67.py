def field(a: int, b: int) -> int:

    return a * b

def solution(x: dict, y: dict) -> int:

    a: int = 0
    b: int = 0

    x1: tuple = (x["top_left"][0], x["top_left"][1])
    x2: tuple = (x["top_left"][0], x["top_left"][1] + x["dimensions"][1])
    x3: tuple = (x["top_left"][0] + x["dimensions"][1], x["top_left"][0])
    x4: tuple = (x2[0] + x["dimensions"][0], x2[1])
    y1: tuple = (y["top_left"][0], y["top_left"][1])
    y2: tuple = (y["top_left"][0], y["top_left"][1] + y["dimensions"][1],)
    y3: tuple = (y["top_left"][0]+ y["dimensions"][0], y["top_left"][1])
    y4: tuple = (y2[0] + y["dimensions"][0], y2[1])
    keyIntersectionPoints: list = []
    intersectPoints: list = [] 

    if x1[0] >= y1[0] and x1[1] >= y1[1] and x1[0] <= y4[0] and x1[1] <= y2[1]:

            keyIntersectionPoints.append('x1')
            intersectPoints.append(x1)

    if y1[0] >= x1[0] and y1[1] >= x1[1] and y1[0] <= x4[0] and x1[1] <= x2[1]:
         
            keyIntersectionPoints.append('y1')
            intersectPoints.append(y1)

    if x2[0] >= y2[0] and x2[1] <= y2[1] and x2[0] <= y4[0]:

            keyIntersectionPoints.append('x2')
            intersectPoints.append(x2)

    if y2[0] >= x2[0] and y2[1] <= x2[1] and y2[0] <= x4[0]:

            keyIntersectionPoints.append('y2')
            intersectPoints.append(y2)

    if x3[0] >= y3[0] and x3[1] >= y3[1] and x3[0] <= y4[0] and x3[1] <= y2[1]:
            
            keyIntersectionPoints.append('x3')
            intersectPoints.append(x3)

    if y3[0] >= x3[0] and y3[1] >= x3[1] and y3[0] <= x4[0] and y3[1] <= x2[1]:
         
            keyIntersectionPoints.append('y3')
            intersectPoints.append(y3)

    if x4[0] >= y4[0] and x4[1] <= y4[1] and x4[0] <= y4[0]:

            keyIntersectionPoints.append('x4')
            intersectPoints.append(x4)

    if y4[0] >= x4[0] and y4[1] <= x4[1] and y4[0] <= x4[0]:

            keyIntersectionPoints.append('y4')
            intersectPoints.append(y4)

    if len(intersectPoints) == 1:
           
           if keyIntersectionPoints[0] == 'x1':
                  a = y2[1] - intersectPoints[0][1]
                  b = y3[0] - intersectPoints[0][0]
           if keyIntersectionPoints[0] == 'y1':
                  a = x2[1] - intersectPoints[0][1]
                  b = x3[0] - intersectPoints[0][0]
           if keyIntersectionPoints[0] == 'x2':
                  a = intersectPoints[0][1] - y1[1]
                  b = y4[0] - intersectPoints[0][0]
           if keyIntersectionPoints[0] == 'y2':
                  a = intersectPoints[0][1] - x1[1]
                  b = x4[0] - intersectPoints[0][0]
           if keyIntersectionPoints[0] == 'x3':
                  a = y3[1] - intersectPoints[0][1] 
                  b = intersectPoints[0][0] - y1[0]
           if keyIntersectionPoints[0] == 'y3':
                  a = x3[1] - intersectPoints[0][1] 
                  b = intersectPoints[0][0] - x1[0]
           if keyIntersectionPoints[0] == 'x4':
                  a = intersectPoints[0][1] - y3[1]
                  b = intersectPoints[0][0] - y2[0]
           if keyIntersectionPoints[0] == 'y4':
                  a = intersectPoints[0][1] - x3[1]
                  b = intersectPoints[0][0] - x2[0]

    elif len(intersectPoints) == 2:
           
           if keyIntersectionPoints[0] == 'x1' and keyIntersectionPoints[1] == 'x2':
                  
                  a = intersectPoints[1][1] - intersectPoints[0][1]
                  b = y4[0] - intersectPoints[0][1]

           if keyIntersectionPoints[0] == 'y1' and keyIntersectionPoints[1] == 'y2':
                  
                  a = intersectPoints[1][1] - intersectPoints[0][1]
                  b = x4[0] - intersectPoints[0][1]

           if (keyIntersectionPoints[0] == 'x1' and keyIntersectionPoints[1] == 'x3') and (keyIntersectionPoints[0] == 'x2' and keyIntersectionPoints[1] == 'x4'):

                  a = y2[1] - intersectPoints[0][1]
                  b = intersectPoints[1][0] - intersectPoints[0][0]

           if (keyIntersectionPoints[0] == 'y1' and keyIntersectionPoints[1] == 'y3') or (keyIntersectionPoints[0] == 'y2' and keyIntersectionPoints[1] == 'y4'):

                  a = x2[1] - intersectPoints[0][1]
                  b = intersectPoints[1][0] - intersectPoints[0][0]

    elif len(intersectPoints) == 3:
           
           if keyIntersectionPoints[0] == 'x2' and (keyIntersectionPoints[1] == 'y3' or keyIntersectionPoints[1] == 'x3') and keyIntersectionPoints[2] == 'x4':
                  
                  a = intersectPoints[0][1] - y1[1]
                  b = y4[0] - intersectPoints[0][0] 

           if keyIntersectionPoints[0] == 'y2' and (keyIntersectionPoints[1] == 'y3' or keyIntersectionPoints[1] == 'x3') and keyIntersectionPoints[2] == 'y4':
                  
                  a = intersectPoints[0][1] - x1[1]
                  b = x4[0] - intersectPoints[0][0]

           if keyIntersectionPoints[0] == 'x1' and (keyIntersectionPoints[1] == 'y4' or keyIntersectionPoints[1] == 'x4' or keyIntersectionPoints[1] == 'y2' or keyIntersectionPoints[1] == 'x2') and keyIntersectionPoints[2] == 'x3':
                  
                  a = y2[1] - intersectPoints[0][1] 
                  b = y3[0] - intersectPoints[0][0]

           if keyIntersectionPoints[0] == 'y1' and (keyIntersectionPoints[1] == 'y4' or keyIntersectionPoints[1] == 'x4' or keyIntersectionPoints[1] == 'y2' or keyIntersectionPoints[1] == 'x2') and keyIntersectionPoints[2] == 'y3':
                  
                  a = x2[1] - intersectPoints[0][1] 
                  b = x3[0] - intersectPoints[0][0]

           if (keyIntersectionPoints[0] == 'y1' or keyIntersectionPoints[0] == 'x1') and (keyIntersectionPoints[1] == 'y4' or keyIntersectionPoints[1] == 'x4' or keyIntersectionPoints[1] == 'y2' or keyIntersectionPoints[1] == 'x2') and (keyIntersectionPoints[2] == 'x4' or keyIntersectionPoints[2] == 'y4'):
                  
                  a = intersectPoints[1][1] - intersectPoints[0][1] 
                  b = intersectPoints[2][0] - intersectPoints[1][0]

    elif len(intersectPoints) == 4:
           
           if keyIntersectionPoints[0] == 'x1':
                  
                  a = x['dimensions'][0]
                  b = x['dimensions'][1]

           if keyIntersectionPoints[0] == 'y1':
                  
                  a = y['dimensions'][0]
                  b = y['dimensions'][1]

    result: int = field(a, b)

    return result

x: dict = {

    "top_left": (1, 4),
    "dimensions": (3, 3)
}
y: dict = {

    "top_left": (0, 5),
    "dimensions": (4, 3)

}
print(solution(x, y))