class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = list(map(lambda x: x[1], sorted(envelopes, key = lambda x: (x[0], -x[1]))))
        dp = [envelopes[0]]
        LONGEST = 1
        import bisect
        for i in range(1, len(envelopes)):
            x = envelopes[i]
            if x > dp[-1]:
                dp.append(x)
                LONGEST += 1
            else:
                index = bisect.bisect_left(dp, x)
                dp[index] = x
        return LONGEST

        
