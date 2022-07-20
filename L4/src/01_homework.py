
def oddOrEven(num):
    if num % 2 == 1:
        print(f'Число {num} є непарним')
    else:
        print(f'Число {num} є парним')

oddOrEven(1)
oddOrEven(20)










def transformStr(str: str):
    transformedStr = str
    if len(str) > 5:
        transformedStr = transformedStr[0:5] + '...'
    if transformedStr[0] in 'Ll': # transformedStr[0] == 'l' or transformedStr[0] == 'L'
        transformedStr = transformedStr.lower()
    elif transformedStr[0] in 'Uu': # transformedStr[0] == 'u' or transformedStr[0] == 'U'
        transformedStr = transformedStr.upper()
    print(transformedStr)

transformStr('Testing string')
transformStr('Lux')
transformStr('up')
transformStr('Luxery')









def sumNum(num):
    tmpNum = num
    while tmpNum > 9:
        tmpRes = 0
        while tmpNum > 9:
            tmpRes += tmpNum % 10
            tmpNum //= 10
        tmpNum += tmpRes
    return tmpNum

print(sumNum(38)) 


def sumNum2(num):
    tmpRes = 0
    while num > 0:
        tmpRes += num % 10
        num = num // 10
        
        if num == 0 and tmpRes > 9:
            num = tmpRes
            tmpRes = 0
            
    return tmpRes






# цікавий факт
def sumNum3(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9


print(sumNum3(3008)) 









## commonStr

## while + string
def commonStr(str1, str2):
    resultStr = ''
    i = 0
    while i < len(str1):
        if str1[i] in str2 and str1[i] not in resultStr:
            resultStr += str1[i]
        i += 1
    return resultStr






## for + list
def commonStrArr(str1, str2):
    resultArr = []
    for ch in str1:
        if ch in str2 and ch not in resultArr:
            resultArr.append(ch)
    return ''.join(resultArr) # convert array to string








## for + set
def commonStrSet(str1: str, str2):
    resultSet = set()
    i = 0
    for ch in str1:
        i += 1
        if ch.isalpha() and ch in str2:
            resultSet.add(ch)
    print(i)
    return ''.join(resultSet) # convert set to string







# for + set (optimization)
def commonStrSet2(str1: str, str2):
    str1Set = set(str1)
    str2Set = set(str2)
    resultSet = set()
    i = 0
    for ch in str1Set:
        i += 1
        if ch.isalpha() and ch in str2Set:
            resultSet.add(ch)
    print(i)
    return ''.join(resultSet)







# for + set (further)
def commonStrSet3(str1: str, str2):
    str1Set = set(str1)
    str2Set = set(str2)
    res = []
    for ch in str1Set.intersection(str2Set):
        if ch.isalpha():
            res.append(ch)
    return ''.join(res)







# for + set (one line)
def commonStrSet4(str1: str, str2):
    return ''.join([ch if ch.isalpha() else '' for ch in set(str1).intersection(set(str2))])


print(commonStrSet4('god \tday', 'good \t morning')) 
