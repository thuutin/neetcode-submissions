class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        if all(map(lambda x: x == 9, digits)):
            return [1] + [0] * len(digits)
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        digits[i] += 1
        return digits

