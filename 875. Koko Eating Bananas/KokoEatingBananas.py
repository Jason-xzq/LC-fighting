class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def IsFinished(speed):
            sum = 0
            for i in piles:
                sum += ((i-1)//speed + 1)
            if sum <= h:
                return True
            else:
                return False
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if not IsFinished(mid):
                low = mid + 1
            else:
                high = mid
        return low