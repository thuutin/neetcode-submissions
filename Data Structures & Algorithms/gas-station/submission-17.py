class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #[-1, 0, -1, 3] [-1, 0, -1, 3]
        #[-1, -1, -2, 1] [0, 0, -1, 3]
        #     [0, -1, 2, 1] 1, 0, 3
        #        [-1, 2, 1, 1] 0, 3
        #             [3, 2, 2, 1] 4
        
        arr = gas[:]
        for i in range(len(arr)):
            arr[i] -= cost[i]
        n = len(gas)
        current = 0
        #print(arr)
        i, j = 0, 0
        while i < n:
            j = max(j, i)
            if current + arr[j % n] >= 0:
                current += arr[j % n]
                if j - i + 1 >= n:
                    return i
                j += 1
            elif i < j:
                current -= arr[i % n]
                i += 1
            else:
                i += 1
        return -1
