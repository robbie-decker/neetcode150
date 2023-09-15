class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hashamapu
        charOccurence = {}
        l = 0
        result = 0
        # Loop through array
        for r in range(len(s)):
            # Add char to dict if not present
            if s[r] not in charOccurence:
                charOccurence[s[r]] = 1
            # Char already there so increase count
            else:
                charOccurence[s[r]] +=1
            # While distinct chars > k s[l]-- in dict and move left pointer
            while sum(charOccurence.values()) - max(charOccurence.values()) > k:
                charOccurence[s[l]] -= 1
                l += 1

            result = max(result, sum(charOccurence.values()))

        return result