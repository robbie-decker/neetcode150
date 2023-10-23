class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # This heap will contain a list of distances and their corresponding
        # coordinates
        distanceAndCoordsHeap = []
        heapq.heapify(distanceAndCoordsHeap)
        for x, y in points:
            # Get distance from origin
            result = sqrt((x**2) + (y**2))
            heapq.heappush(distanceAndCoordsHeap, [result, [x,y]])
        resultCoords = []
        # This will append the k smallest coords from heap
        for i in range(k):
            resultCoords.append(heapq.heappop(distanceAndCoordsHeap)[1])
        return resultCoords