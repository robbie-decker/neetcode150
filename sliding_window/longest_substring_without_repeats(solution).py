class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = []
        l = 0
        result = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.pop(0)
                l += 1
            charSet.append(s[r])
            result = max(result, r - l + 1)
        return result