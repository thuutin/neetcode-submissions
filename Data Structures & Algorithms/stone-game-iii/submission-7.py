class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        alice = [float("-inf")] * len(stoneValue)
        bob = [float("inf")] * len(stoneValue)
        alice[-1] = stoneValue[-1]
        bob[-1] = -stoneValue[-1]
        for i in range(len(stoneValue) - 2, -1, -1):
            s = 0
            for j in range(i + 1, min(i + 4, len(stoneValue) + 1)):
                s += stoneValue[j - 1]
                alice[i] = max(alice[i], s + (bob[j] if j < len(stoneValue) else 0))
                bob[i] = min(bob[i], -s + (alice[j] if j < len(stoneValue) else 0))
        score = alice[0]

        if score > 0:
            return "Alice"
        elif score == 0:
            return "Tie"
        else:
            return "Bob"