# Solution uses Quick Select algo, but it kept timing out
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Index in array we want to find
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                # swap val with p val is
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            # swap pivot val and p val
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:   return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else:       return nums[p]

        return quickSelect(0, len(nums) - 1)