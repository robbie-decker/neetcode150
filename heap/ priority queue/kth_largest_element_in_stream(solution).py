class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with k largest integers
        self.minHeap, self.k = nums, k
        # Turn into heap
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            # pop min value
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # heap is greater than k so pop
        if len(self.minHeap) >= self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]