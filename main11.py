def isPalindrome(text: str) -> bool:

        it: int = 0
        textLength = len(text)

        for _ in range(textLength - 1):

            if text[it] != text[textLength - it - 1]:
                 
                return False

            it += 1
            
        return True

def solution(text: str) -> str:

    maxText: str = ''
    maxLength: int = 0
    textLength: int = 0
    text0: str = ''
    text1: str = ''
    text2: str = ''
    finalText: str = ''
    it: int = 0

    for _ in range(len(text) - 1):

        text0 = text[it:]
        text1 = text[it:len(text) - it]
        text2 = text[:len(text) - it]

        if isPalindrome(text0):
            finalText = text0
        elif isPalindrome(text1):
            finalText = text1
        elif isPalindrome(text2):
             finalText = text2
              
        textLength = len(finalText)

        if textLength > maxLength:
                   
            maxLength = textLength

            maxText = finalText

        it += 1

    return maxText

print(solution("aabcdcb"))