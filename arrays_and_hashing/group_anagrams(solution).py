class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Suprisingly I think the way I solved this was better. It had a faster time and used less memory

        res = defaultdict(list) # mapping charCount to list of Anargrams

        for s in strs:
            count = [0] * 26 # a...z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()