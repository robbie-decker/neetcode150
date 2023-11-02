class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i >= len(nums):
                # Do not use reference. Want a full copy
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # All subsets that don't include nums[i]
            subset.pop()
            # [1,2,2].  Trying to skip the second 2
            # Just trying to increment i to a new value
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        backtrack(0,[])
        return res