class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        myHeap = []
        heapq.heapify(myHeap)
        taskCount = {}
        for x in tasks:
            if x not in taskCount:
                taskCount[x] = 1
            else:
                taskCount[x] += 1
            heapq.heappush(myHeap, [-taskCount[x], x])

        #  Need to account for cooldown here
        count = 0
        while myHeap:
            test = heapq.heappop(myHeap)
            print(test)
            count+=1

        return count