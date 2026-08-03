class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        # ["Hello","World"]
        # "5#Hello5#World"
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = 0
            while i < len(s) and s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            res.append(s[i:i + length])
            i += length
        return res
            
