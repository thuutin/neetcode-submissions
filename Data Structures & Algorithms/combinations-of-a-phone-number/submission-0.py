class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_chars = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        res = [""]
        for d in digits:
            combinations = []
            for prev_combination in res:
                for c in digit_to_chars[int(d)]:
                    combinations.append( prev_combination + c)
            res = combinations
        return res
