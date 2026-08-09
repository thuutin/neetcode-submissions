class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        #[3,1,5,4,2,3,4,2]
        #2,1,1,2,2,1,1,2
        res = 0
        prev = 0
        for i, x in enumerate(target):            
            if x > prev:
                res += x - prev
            prev = x
        return res