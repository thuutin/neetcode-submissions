class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            s = str(len(s)) + "#" + s
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s): 
            j = i
            while s[j] != '#':      
                j += 1
            n = int(s[i:j])
            decoded.append(s[j + 1: j + n + 1])
            i = j + n + 1
        return decoded
