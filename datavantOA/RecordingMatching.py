def match_records(input_data):
    # Write your code here
    size = len(input_data) - 1
    res = []
    for i in range(size):
        inner = []
        for j in range(size):
            inner.append(0)
        res.append(inner)
    # print(res)
    after = []
    dict = {}
    # after_ele = []
    for i in range(1, len(input_data)):
        after_ele = input_data[i].split(",")
        after.append(after_ele)
    for i in range(size):
        for j in range(size):
            if after[i][0] == after[j][0] or after[i][1] == after[j][1] or after[i][2] == after[j][2]:
                res[i][j] = 1
                if i not in dict:
                    dict[i] = [j]
                else:
                    dict[i].append(j)

    for i in range(size):
        for ii in range(len(dict[i])):
            for ij in range(ii + 1, len(dict[i])):
                res[ii][ij] = 1
    return res