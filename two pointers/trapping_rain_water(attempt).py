class Solution:
    def trap(self, height: List[int]) -> int:
        # I COULDN'T GET THIS WORKING :(((((
        l = 0
        water = 0
        while l <= len(height) - 1:
            if height[l] == 0:
                l += 1
            else:
                r = l + 1
                if r > len(height) - 1:
                    return water
                while height[l] >= height[r]:
                    print(l,r)
                    r += 1
                    if r > len(height) - 1:
                        return water
                for i in range(l,r):
                    water = water + (min(height[l], height[r]) - height[i])
                l = r