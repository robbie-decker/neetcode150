# Here is my binary search attempt

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Sorted off rip
        self.nums = list(nums)
        self.nums.sort()

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
            return val
        # Can binary search this John
        l,r = 0, len(self.nums) - 1
        m = 0
        while l <= r:
            m = (l + r) // 2
            if val > self.nums[m]:
                l = m + 1

            elif val < self.nums[m]:
                r = m - 1

            else:
                break
        # self.nums.insert(m+1, val) if m else self.nums.append(val)
        if val > self.nums[m]:
            self.nums.insert(m+1, val)
        else:
            self.nums.insert(m, val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)




# Here is my popping and max attempt
# This idea was too slow to submit
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = list(nums)

    def add(self, val: int) -> int:
        self.nums.append(val)
        poppedNums = []

        for i in range(self.k):
            maxNum = max(self.nums)
            poppedNums.append(self.nums.pop(self.nums.index(maxNum)))
        self.nums = self.nums + poppedNums
        return poppedNums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)