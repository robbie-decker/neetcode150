# Time complexity (I think) O(2^n n*log(n))

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = [] 

        def dfs(i):
            if i >= len(nums):
                # O (nlog(n))
                sortedSubset = sorted(subset.copy())
                if sortedSubset not in res:
                    res.append(sortedSubset)
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res