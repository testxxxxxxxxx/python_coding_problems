def isPalindrome(text: list) -> bool:

        for i in range(len(text)):

            if text[i] != text[len(text) - 1 - i]:

                return False
            
        return True

def solution(text: str, k: int) -> bool:

    count: int = 0
    textArr: list = list(text)
    textArr0: list = list(text)
    textArr1: list = list(text)

    for i in range(len(textArr)):

        if i == len(textArr):
             break

        if textArr[i] != textArr[len(textArr) - 1 - i]:

            textArr.pop(len(textArr) - 1 - i)
            count += 1

        if count == k:
            break

    count = 0

    for j in range(len(textArr0)):
         
         if j == len(textArr0):
              break
         
         if textArr0[j] != textArr0[len(textArr0) - 1 - j]:
              textArr0.pop(j)
              count += 1

         if count == k:
            break
         
    count = 0

    for x in range(len(textArr1)):
         
        if x == len(textArr1):
            break
         
        if textArr1[x] != textArr1[len(textArr1) - 1 - x]:
            textArr1.pop(len(textArr1) - 1 - x)
            textArr1.pop(x)
            count += 1

        if count == k:
            break

    print(textArr)
    print(textArr0)
    print(textArr1)

    if isPalindrome(textArr) or isPalindrome(textArr0) or isPalindrome(textArr1):
         return True
    
    return False

def solution0(text: str, k: int):

    letters: str = text[0:len(text)//2 - 1]
    halfText: list = list(text[len(text)//2 - 1:])

    halfText.reverse()

    count: list = [1 for i in range(len(letters))]

    for j in range(len(halfText)):

        print(letters[j%len(letters)])
        print(halfText[j])

        if letters[j%len(letters)] == halfText[j]:

            count[j%len(letters)] += 1


    print(count)

print(solution('waterrfetawx', 2))
print(solution0('watferretawx' , 2))