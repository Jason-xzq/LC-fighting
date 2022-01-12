class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval[0], newInterval[1]
        inserted = []
        placed = False
        for interval in intervals:
            if interval[1] < left:
                inserted.append(interval)
            elif interval[0] > right:
                if not placed:
                    inserted.append([left, right])
                    placed = True
                inserted.append(interval)
            else:
                left = min(left, interval[0])
                right = max(right, interval[1])
        if not placed:
            inserted.append([left, right])
        return inserted
    