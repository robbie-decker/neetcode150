class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate list
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # remember we negated the array. 
            if second > first:
                heapq.heappush(stones, first - second)

        # Could have empty array
        stones.append(0)
        return abs(stones[0])