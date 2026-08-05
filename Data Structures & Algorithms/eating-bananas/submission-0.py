class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatWithRate(k):
            hours_needed = 0
            for p in piles:
                hours_needed += p // k
                if p % k > 0:
                    hours_needed += 1
                if hours_needed > h:
                    return False
            return True

        start = 1
        end = max(piles)
        while start < end:
            mid = (start + end) // 2
            if canEatWithRate(mid):
                end = mid
            else:
                start = mid + 1
        return start