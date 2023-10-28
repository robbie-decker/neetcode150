class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This line will convert our set int a list of lists
        # Pretty slick and it uses list comprehension
        numSet = set()
        numSet.add(())
        res = [[x] if type(x) is int  else list(x) for x in numSet]
        # for 
        # I think this is as far as I can get :/
        # return res
        # Dumb one liner that I found that works really well
        # return [[nums[j] for j in range(len(nums)) if i >> j & 1] for i in range(2 ** len(nums))]