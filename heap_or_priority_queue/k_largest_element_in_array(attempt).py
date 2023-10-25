class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Set all nums to a negative value
        nums = [-x for x in nums]
        # make nums a heap, since all nums are negative we
        # effectively make a max heap
        heapq.heapify(nums)
        # Pop until we get the value we want
        for i in range(k):
            res = heapq.heappop(nums)

        # Return the negative value to flip back to normal
        return -res