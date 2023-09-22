class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # Might encounter an overflow (2^31) using below method
            m = (l + r) // 2

            # If asked to solve the overflow then you can do
            #  m = l + ((r - l) // 2)
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else: 
                return m
        return -1