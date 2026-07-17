class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)

        first = strs[0]
        last = strs[-1]
        p = 0
        for p in range(min(len(first), len(last))):
            if first[p] != last[p]:
                return first[:p]
        return first[:p+1]
        