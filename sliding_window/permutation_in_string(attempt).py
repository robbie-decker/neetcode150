# This was really close to working. Ended up getting 92/ 108 testcases passed

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        result = False
        l = 0
        s1_copy = list(s1)
        currentWindow = []
        for r in range(len(s2)):
            # We found a match
            if s2[r] in s1_copy:
                # Remove current char from copy
                charOccurence = s1_copy.index(s2[r])
                s1_copy.pop(charOccurence)
                # If copy = 0 then we found our substring
                if len(s1_copy) == 0:     
                    result = True
            else:
                # A copy of something already taken out
                if s2[r] in s1:
                    while s2[l] != s2[r]:
                        s1_copy.insert(0, s2[l])
                        l+=1
                # Char is not a copy so reset window
                else:
                    s1_copy = list(s1)
                    l = r
        return result