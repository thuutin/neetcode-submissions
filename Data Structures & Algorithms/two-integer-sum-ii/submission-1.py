class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            x = numbers[i]
            y = numbers[j]
            if x + y == target:
                return [i + 1, j + 1]
            if x + y > target:
                j -= 1
            else:
                i += 1
        return None