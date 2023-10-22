class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negativeStones = [-x for x in stones]
        heapq.heapify(negativeStones)

        while len(negativeStones) > 1:
            y = abs(heapq.heappop(negativeStones))
            x = abs(heapq.heappop(negativeStones))
            result = y - x
            if y-x != 0:
                heapq.heappush(negativeStones, -(y-x))
            
        if negativeStones:
            return abs(negativeStones[0])
        else:
            return 0        