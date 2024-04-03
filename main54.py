from random import randint

def silnia(n: int) -> int:

    if n <= 1:
        return 1
    
    return n*silnia(n - 1)

def getPermutation(text: str) -> str:

    result: str = ''
    chosenLetters: list = []
    letter: int = randint(0, len(text) - 1)

    for _ in range(len(text)):

        while True:

            letter = randint(0, len(text) - 1)

            if findArr(chosenLetters, letter):
                break

        result += text[letter]
        chosenLetters.append(letter)

    return result 

def findArr(arr: list, value) -> bool:

    for i in arr:

        if i == value:
            return False
        
    return True

def isPalindome(text: str) -> bool:

    for i in range(len(text)):

        if text[i] != text[len(text) - i - 1]:
            return False
        
    return True

def getNumberOfLetters(text: str) -> list:

    keys: list = []
    letters: list = [1 for i in range(len(set(text)))]

    for i in range(len(text)):

        if findArr(keys, text[i]):
            keys.append(text[i])
        else:
            index: int = keys.index(text[i])
            letters[index] += 1

    return letters

def getPermutationWithN(letters: list, text: str) -> int:

    length: int = len(text)
    sumSil: int = 1

    for i in letters:

        sumSil *= silnia(i)

    return (silnia(length)//sumSil)

def solution(text: str) -> bool:

    letters0: list = getNumberOfLetters(text)
    numberOfPermutations: int = getPermutationWithN(letters0, text)
    permutation: str = ''
    permutations: list = []

    for i in range(numberOfPermutations):

        while True:

            permutation = getPermutation(text)

            if findArr(permutations, permutation) and permutation != '':
                break

        permutations.append(permutation)

    for i in permutations:

        if isPalindome(i):
            return True
        
    return False

print(solution("carrace"))