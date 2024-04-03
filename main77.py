def solution(str0: str, str1: str, str2: str) -> int:

    def findArr(arr: list, value: int) -> bool:

        for i in arr:

            if i == value:
                return True
            
        return False

    def findInStr(str0: str, str1: str) -> str:

        strList1: list = list(str1)
        result: str = ''
        foundedLetters: list = []

        for i in range(len(str0)):

            for j in range(len(str1)):

                if str0[i] == str1[j]:
                    foundedLetters.append(j)
                    break

        for i in foundedLetters:

            if i != '':
                result += strList1[i]

        return result

    strList0: list = list(str0)
    strList1: list = list(str1)
    strList2: list = list(str2)
    found0: bool = False
    found1: bool = False
    found2: bool = False
    it0: int = 0
    it1: int = 0
    result: str = ''
    results: list = []

    for i in range(len(strList0)):

        selectLetter: str = strList0[i]

        found0 = False
        found1 = False

        for j in range(len(strList1)):

            if selectLetter == strList1[j] and strList1[j] != '':
                strList1[j] = ''
                found0 = True
                it0 += 1
                break
        
        for x in range(len(strList2)):

            if selectLetter == strList2[x] and strList2[x] != '':
                strList2[x] = ''
                found1 = True
                it1 += 1
                break

        if found0 and found1:
            result += selectLetter


    results.append(findInStr(str0, result))
    results.append(findInStr(str1, result))
    results.append(findInStr(str2, result))

    result = ''

    maxStr: str = results[2]

    print(results)

    it: int = 0
    it0: int = 0
    it1: int = 0

    for i in range(len(maxStr)):

        found0 = False
        found1 = False
        found2 = False

        if maxStr[i % len(maxStr)] == results[0][it % len(results[0])]:
            if it <= len(results[0]) - 1:
                it += 1
            found0 = True

        if maxStr[i % len(maxStr) ] == results[1][it0 % len(results[1])]:
            if it0 <= len(results[1]) - 1:
                it0 += 1
            found1 = True

        if maxStr[i% len(maxStr)] == results[2][it1 % len(results[2])]:
            if it1 <= len(results[2]) - 1:
                it1 += 1
            found2 = True
            
        if found0 and found1 and found2:
            result += maxStr[i % len(maxStr)]
        
    print(result)

    maxLen: int = len(result)

    return maxLen

print(solution("supercalifragilisticexpialodocious", "refrigeration", "epidemiologist"))