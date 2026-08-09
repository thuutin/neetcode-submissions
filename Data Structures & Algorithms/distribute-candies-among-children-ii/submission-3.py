class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for a in range(max(0, n - limit*2), min(limit, n) + 1):
            left = n - a
            if left > 2 * limit:
                continue
            if left > limit:
                minValue = left - limit
                maxValue = limit
                res += abs(maxValue - minValue) + 1
            else:
                res += left + 1
        return res
        #x 
        #n - a <= limit * 2
        # 
