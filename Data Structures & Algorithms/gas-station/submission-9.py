class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #[-1, 0, -1, 3] [-1, 0, -1, 3]
        #[-1, -1, -2, 1] [0, 0, -1, 3]
        #     [0, -1, 2, 1] 1, 0, 3
        #        [-1, 2, 1, 1] 0, 3
        #             [3, 2, 2, 1] 4
        arr = []
        for i in range(len(gas)):
            arr.append(gas[i] - cost[i])
        pref = []
        n = len(gas)
        prev = 0
        for i in range(len(arr) * 2):
            prev += arr[i % len(arr)]
            pref.append(prev)
        # elemn  >= x
        minH = []
        empty = 0
        #print(pref)
        for i, p in enumerate(pref[:-1]):
            heapq.heappush(minH, (p, i))
            if i >= n - 1:
                while minH and minH[0][1] <= i - n:
                    heapq.heappop(minH)
                if minH and minH[0][0] >= empty:
                    return i - n + 1
                empty = pref[i + 1 - n]
        return -1
        
            
            