class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        from functools import cache
        @cache
        def dp(i, alice):
            if i >= len(stoneValue):
                return 0
            neg = 1 if alice else -1
            choices = []
            s = 0
            for j in range(i + 1, i + 4):
                if j - 1 >= len(stoneValue):
                    break 
                s += stoneValue[j - 1]
                choices.append(neg * s + dp(j, not alice))
            return max(choices) if alice else min(choices)

        #dp(i, alice_turn) returns the score of alice - score of bob
        score = dp(0, True)
        if score > 0:
            return "Alice"
        elif score == 0:
            return "Tie"
        else:
            return "Bob"