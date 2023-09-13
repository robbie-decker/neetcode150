class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        substring = []
        myMax = 0
        if len(s) <= 1:
            return len(s)

        substring.append(s[l])
        while r < len(s):
            if s[r] in substring:
                print(r, s[r])
                print(len(substring))
                if len(substring) > myMax:
                    myMax = len(substring)
                substring.clear()
                l+=1
                r = l
                
            else:
                substring.append(s[r])
                r+=1
        if len(substring) > myMax:
                    myMax = len(substring)
        return myMax