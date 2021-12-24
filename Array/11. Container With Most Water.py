class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mostWater = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] <= height[right]:
                left += 1
                mostWater = max(mostWater, min(height[left], height[right]) * (right - left))
            else:
                right -= 1
                mostWater = max(mostWater, min(height[left], height[right]) * (right - left))
        return mostWater
