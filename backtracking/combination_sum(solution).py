class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # i = pointer, cur = array used so far, total = sum of array
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            # Path we have taken is not possible
            if i >= len(candidates) or total > target:
                return
            
            # Include candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Do not include candidate
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res