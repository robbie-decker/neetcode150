class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                copy = cur.copy()
                # copy.sort()
                if copy not in res:
                    res.append(copy)
                return

            if i >= len(candidates) or total > target:
                return
            
            # include
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])

            # do not include and of these nums and skip
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res