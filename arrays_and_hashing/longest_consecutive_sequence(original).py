class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # My version
        nums = set(nums)
        consecutive = 0
        for x in nums:
            temp, runStatus = 0, True
            if x-1 in nums:
                continue
            else:
                factor = 0
                while runStatus:
                    if x + factor in nums:
                        temp += 1
                        factor += 1
                    else:
                        runStatus = False
                if temp > consecutive:
                    consecutive = temp

        return consecutive