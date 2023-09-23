# Could not get this to not timeout
from functools import reduce

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        summation = reduce(lambda a,b: a+b, piles)
        l, r = 0, piles[-1]
        currentMin = r
        while l <= r:
            piles_copy = piles.copy()
            print(currentMin)
            m = (l + r) // 2
            rateWorks = self.doesRateWork(m, piles_copy, h)

            if rateWorks:
                currentMin = min(currentMin, m)
                r = m -1
            else:
                l = m + 1
        return currentMin

    # I blame this function for my timeouts
    def doesRateWork(self, rate, piles, h):
        hours = 0
        while piles:
            piles[0] -= rate
            hours+=1
            if hours > h:
                return False
            if piles[0] <= 0:
                piles.pop(0)
        return True
            