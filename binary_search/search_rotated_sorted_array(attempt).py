class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # We are in left sorted so check for target
            if nums[m] >= nums[l]:
                # Target is in left sorted so move r
                if nums[m] > target and nums[l] <= target:
                    r = m - 1
                # Target not here so move l
                else:
                    l = m + 1
            # We are in right sorted
            else:
                # Target is in right sorted
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                # Target is not here, move r
                else:
                    r = m - 1
        return -1