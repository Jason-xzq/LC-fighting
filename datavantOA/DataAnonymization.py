def tokenize(input_data):
    # Write your code here

    res = []
    res.append("Date of Visit,Diagnostic Code,Token1,Token2")
    # splitted = []
    for i in range(1, len(input_data)):
        splitted = input_data[i].split(",")
        # print(splitted)
        if len(splitted) != 6:
            continue
        after = splitted[3] + "," + splitted[5]
        if len(splitted[0]) == 0 or len(splitted[1]) == 0:
            after += ",,"
        if len(splitted[0]) != 0 and len(splitted[1]) != 0:
            Token1 = len(splitted[0]) + len(splitted[1])
            after += "," + str(Token1) + ","
        if len(splitted[2]) == 5 and len(splitted[4]) == 11:
            num1 = int(splitted[2][2:])
            num2 = int(splitted[4][:3])
            after += str(num1 + num2)
        res.append(after)
    return res