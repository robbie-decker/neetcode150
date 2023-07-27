class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        maxLength = 10**5
        maxNum = 10**9
        if 1 <= len(nums) <= maxLength:
            for i in nums:
                if -(maxNum) <= i <= maxNum:
                    if(nums.count(i) > 1):
                        return True
                else: return False
            return False
        else:
            return False