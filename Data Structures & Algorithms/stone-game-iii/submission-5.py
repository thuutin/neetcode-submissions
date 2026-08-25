class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        alice = [float("-inf")] * len(stoneValue)
        bob = [float("inf")] * len(stoneValue)
        alice.append(0)# = 0
        bob.append(0)# = 0
        for i in range(len(stoneValue) - 1, -1, -1):
            s = 0
            for j in range(i + 1, min(i + 4, len(stoneValue) + 1)):
                s += stoneValue[j - 1]
                alice[i] = max(alice[i], bob[j] + s)
                bob[i] = min(bob[i], alice[j] - s)
        score = alice[0]

        if score > 0:
            return "Alice"
        elif score == 0:
            return "Tie"
        else:
            return "Bob"