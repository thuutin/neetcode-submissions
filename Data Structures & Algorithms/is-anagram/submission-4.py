class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        for c in t:
            arr[ord(c) - ord('a')] -= 1
            
        return all(map(lambda x: x==0, arr))