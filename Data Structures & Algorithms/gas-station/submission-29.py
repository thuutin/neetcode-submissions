class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        current = 0
        #print(arr)
        i, j = 0, 0
        while i < n:
            if current + gas[j % n] - cost[j%n] >= 0:
                current += gas[j % n] - cost[j%n]
                if j - i + 1 >= n:
                    return i
                j += 1
            elif i <= j:
                if i < j:
                    current -= (gas[i % n] - cost[i%n])
                i += 1

            j = max(j, i)
        return -1
