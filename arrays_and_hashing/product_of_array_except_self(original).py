class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            prefix_prod, suffix_prod = 1, 1
            prefix = nums[:i]
            for x in prefix:
                prefix_prod = prefix_prod * x 
            suffix = nums[i + 1:]
            for y in suffix:
                suffix_prod = suffix_prod * y
            answer.append(prefix_prod * suffix_prod)
        return answer 