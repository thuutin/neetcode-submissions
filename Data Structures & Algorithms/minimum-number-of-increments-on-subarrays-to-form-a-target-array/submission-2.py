class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        #[3,1,5,4,2,3,4,2]
        #2,1,1,2,2,1,1,2
        res = 0
        for i, x in enumerate(target):
            if i == 0:
                res += x
            if i > 0:
                if x <= target[i - 1]:
                    res += 0
                else:
                    res += x - target[i - 1]
        return res