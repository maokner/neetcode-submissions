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
            numDigits = 0
            curr = idx
            numVals = 0
            while s[curr] != "#":
                numVals = numVals*10 + int(s[curr])
                numDigits += 1
                curr += 1
            ret.append(s[idx+numDigits + 1:idx + numDigits + 1 + numVals])
            idx = idx+numDigits + 1 + numVals
        return ret