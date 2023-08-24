class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            tempArea = 0
            length = right - left
            tempArea = height[right] * length  if height[left] >= height[right] else height[left] * length
            if tempArea > maxArea:
                maxArea = tempArea 
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return maxArea
