class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []
        x = 0
        y = 1
        print(len(nums))
        if len(nums) > 10000:
                return
        while x < len(nums) and x < 10000:
            while y < len(nums) and y < 10000:
                if(nums[x] + nums[y] == target):
                    temp.append(x)
                    temp.append(y)
                    return temp
                y+=1
            x+=1
            y = x + 1
        return temp