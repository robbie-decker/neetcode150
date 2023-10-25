class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task is 1 unit of time
        # minimize idle time

        # Time complexity O(n * m)
        # n = length of tasks
        # m = idleTime (or the n input)


        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pair of [-cnt, idleTime (time to add back to heap)]

        while maxHeap or q:
            time += 1

            if maxHeap:
                # add instead of subtract because vals are negative
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time