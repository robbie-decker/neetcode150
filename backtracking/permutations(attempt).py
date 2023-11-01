class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        perm = []
        # Backtracking using DFS
        def backtrack(nums):
            if len(nums) <= 0:
                res.append(perm.copy())
                perm.clear()
                return


            for i in range(len(nums)):
                perm.append(nums[i])
                temp = nums.copy()
                temp.pop(i)
                backtrack(temp)

        backtrack(nums)
        return res