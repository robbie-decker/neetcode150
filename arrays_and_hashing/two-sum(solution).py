class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_val_index = {}
        for i, val in enumerate(nums):
            if target - val not in nums_val_index:
                nums_val_index[val] = i
            else:
                return [nums_val_index[target - val], i]
        return [0,0]