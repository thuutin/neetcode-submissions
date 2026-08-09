class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def noZero(arr):
            if len(arr) == 0:
                return 0
            pref = []
            last = 1
            for x in arr:
                pref.append(last * x)
                last = pref[-1]
            maxP = pref[0]
            neg = []
            pos = []
            for i in range(1, len(arr)):
                prev = pref[i-1]
                if prev < 0:
                    heapq.heappush(neg, -prev)
                else:
                    heapq.heappush(pos, prev)
                maxP = max(maxP, pref[i])
                if pref[i] > 0 and pos:
                    P = pref[i] // pos[0] 
                    maxP = max(P, maxP)   
                elif pref[i] < 0 and neg:
                    P = pref[i] // -neg[0]    
                    maxP = max(P, maxP)
            return maxP
        last = 0
        P = []
        for i in range(len(nums)):
            if nums[i] == 0:
                P.append(0)
                P.append(noZero(nums[last:i]))
                last = i + 1
        P.append(noZero(nums[last:len(nums)]))
        return max(P)