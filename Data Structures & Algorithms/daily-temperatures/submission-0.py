class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        H = {}
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            future = None
            for x in range(t + 1, 101):
                if x in H:
                    if future == None or future > H[x]:
                        future = H[x]
            if future:
                res[i] = future - i
            H[t] = i
        return res
