class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(candidates)):
            for j in range(i, len(candidates)):
                print(j)