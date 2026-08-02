class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            s = str(len(s)) + "#" + s
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        n = 0
        i = 0
        while i < len(s): 
            c = s[i]
            if c.isdigit():
                n = n * 10 + int(c)
                i += 1
            if c == '#':
                decoded.append(s[i + 1: i + n + 1])
                i += n + 1
                n = 0
        return decoded
