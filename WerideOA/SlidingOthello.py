# Enter your code here. Read input from STDIN. Print output to STDOUT

# Not bug free!
def main():
    def move(movedepth, rowId, colId, rowDis, colDis):
        newRowId = rowId + rowDis
        newColId = colId + colDis
        if newColId < 0 or newColId >= 5 or newRowId < 0 or newRowId >= 5:
            return;
        color = board[rowId][colId]
        board[newRowId][newColId] = color
        board[rowId][colId] = 0
        movedepth += 1
        if checkSuccess(board):
            return

        return


    # def move_back(rowId, colId, rowDis, colDis):
    #     newRowId = rowId + rowDis
    #     newColId = colId + colDis
    #     if newColId < 0 or newColId >= 5 or newRowId < 0 or newRowId >= 5:
    #         return
    #     color = board[newRowId][newColId]
    #     board[rowId][colId] = color
    #     board[newRowId][newColId] = 0
    #     return
    def checkSuccess(board):
        flag = True
        for colId in range(len(board[0])/2):
            for rowId in range(len(board)):
                if board[rowId][colId] == 2:
                    flag = False
                    return flag
        for colId in range(len(board[0])/2, len(board[0])):
            for rowId in range(len(board)):
                if board[rowId][colId] == 1:
                    flag = False
                    return flag

        return flag

    board = []

    inputString = input()
    inputList = inputString.split(" ")
    rowNum = inputList[0]
    colNum = inputList[1]
    # print(rowNum)
    # print(colNum)
    for i in range(int(rowNum)):
        row = []
        inputRow = input()
        # inputRowSplited = inputRow.split("")
        # print(inputRow)
        for j in inputRow:
            row.append(int(j))
        # print(row)
        board.append(row)
        # print(board)

    # print(board)

    for rowId in range(len(board)):
        for colId in range(len(board[0])):
            if board[rowId][colId] == 0:
                vacRow = rowId
                vacCol = colId
                break;

    movedepth = 0
    move(vacRow, vacCol, 0, 1)






if __name__ == "__main__":
    main()