class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for l in range(len(temperatures)):
            r = l + 1
            count = 0
            while r < len(temperatures):
                count+= 1
                if temperatures[r] > temperatures [l]:
                    result.append(count)
                    break
                r+=1
            if r == len(temperatures):
                result.append(0)
        return result