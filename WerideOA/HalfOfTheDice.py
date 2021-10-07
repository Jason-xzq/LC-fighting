import sys


def main():
    numbers = input()
    numbersList = numbers.split(" ")
    dict = {}
    # print(type(numbersList[0]))
    # print(numbersList)
    possibility = []
    possibility.append([0, 1, 2])
    possibility.append([0, 2, 3])
    possibility.append([1, 2, 4])
    possibility.append([2, 3, 4])
    possibility.append([1, 4, 5])
    possibility.append([3, 4, 5])
    possibility.append([0, 1, 5])
    possibility.append([0, 3, 5])
    # print(possibility)
    for possiIndex in range(8):
        firstNumIndex = possibility[possiIndex][0]
        firstNum = int(numbersList[firstNumIndex])
        secondNumIndex = possibility[possiIndex][1]
        secondNum = int(numbersList[secondNumIndex])
        thirdNumIndex = possibility[possiIndex][2]
        thirdNum = int(numbersList[thirdNumIndex])
        sum = firstNum + secondNum + thirdNum
        if sum not in dict:
            dict[sum] = 1

    result = list(dict.keys())
    result.sort()
    # for i in range(len(dict)):
    #     result.append(dict.pop(i))
    # result.sort()
    # print(dict)
    print(len(result))
    resultString = ""
    for i in result:
        resultString += str(i) + " "
    print(resultString)




if __name__ == "__main__":
    main()