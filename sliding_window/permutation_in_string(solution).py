class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26
        # Count chars of each string for size of s1
        for i in range(len(s1)):
            # Adds 1 to letter by the index it is in the alphabet
            s1Count[ord(s1[i]) - ord('a')] += 1 
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        # Get number of matches between hashmaps at start
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True

            # map current char to index (add r to window)
            index = ord(s2[r]) - ord('a')
            # char just added to window so increase count
            s2Count[index] += 1
            # We found a match!
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Count before adding was equal
            # We added something that does not match :/
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Now remove l from window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # Removing added a match!
            if s1Count[index] == s2Count[index]:
                matches += 1
            # Count before removing was equal
            # Removing added something that does not match
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26