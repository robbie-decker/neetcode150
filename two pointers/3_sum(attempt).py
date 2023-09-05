# This attempt was too slow to submit :(
# And it was so close to the right answer man
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []

        for i in range(len(nums) - 1):
            left, right = 0, len(nums) - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum < 0:
                    left += 1
                elif curSum > 0:
                    right -= 1
                else:
                    if i != left and i != right:
                        curTriplet = sorted([nums[i], nums[left], nums[right]])
                        if curTriplet not in triplets:
                            triplets.append(curTriplet)
                    right -= 1
        return triplets