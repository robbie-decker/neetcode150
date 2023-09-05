class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProf = 0
        while r < len(prices):
            leftValue = prices[l]
            rightValue = prices[r]
            if leftValue > rightValue:
                l = r
                r += 1
            else:
                tempProf = rightValue - leftValue
                if tempProf > maxProf: maxProf = tempProf
                r += 1
        return maxProf
            