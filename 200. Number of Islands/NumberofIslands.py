

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        columnLen = len(grid[0])
        count = 0

        def dfs(rowId, columnId):
            if rowId < 0 or rowId >= rowLen or columnId < 0 or columnId >= columnLen or grid[rowId][columnId] == '0':
                return
            if grid[rowId][columnId] == '1':
                grid[rowId][columnId] = '0'
                dfs(rowId-1, columnId)
                dfs(rowId+1, columnId)
                dfs(rowId, columnId-1)
                dfs(rowId, columnId+1)


        for rowId in range(rowLen):
            for columnId in range(columnLen):
                if grid[rowId][columnId] == '1':
                    count += 1
                    dfs(rowId, columnId)

        return count

