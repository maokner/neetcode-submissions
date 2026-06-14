class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for s in strs:
            ret.append(f"{len(s)}#{s}")
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        ret = []
        idx = 0
        while idx<len(s):
            j = idx
            while s[j] != "#":
                j += 1
            length = int(s[idx:j])
            idx = j+1
            ret.append(s[idx:idx+length])
            idx += length
        return ret