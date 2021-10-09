
#need more shortcut
#should consider space complexity
#could consider bit operation
def solution(N, K):
    # write your code in Python 3.6
    list = []
    for i in range(N, 0, -1):
        list.append(i)

    ktmp = K
    count = 0
    for i in list:
        ktmp -= i
        count += 1
        if ktmp < 0:
            ktmp += i
            count -= 1
        if ktmp == 0:
            return count
    if ktmp > 0:
        return -1
    pass



def solution(A):
    # write your code in Python 3.6
    dict = {}
    max = -1
    for i in A:
        sum = 0
        itmp = i
        while itmp > 0:
            sum += itmp % 10
            itmp = itmp // 10
        if sum in dict and len(dict[sum]) == 1:
            dict[sum].append(i)
            maxtmp = dict[sum][0] + dict[sum][1]
            if maxtmp > max:
                max = maxtmp

        elif sum in dict and len(dict[sum]) == 2:
            if i > dict[sum][0] or i > dict[sum][1]:
                if dict[sum][0] > dict[sum][1]:
                    dict[sum].pop(1)
                else:
                    dict[sum].pop(0)
                dict[sum].append(i)
                maxtmp = dict[sum][0] + dict[sum][1]
                if maxtmp > max:
                    max = maxtmp
        elif sum not in dict:
            dict[sum] = [i]


    print("max: " + str(max))
    print(str(dict))

    pass
A = [27, 72, 36, 37, 73, 89, 98]
solution(A)