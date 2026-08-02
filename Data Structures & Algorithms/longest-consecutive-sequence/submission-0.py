class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        above = {}
        below = {}
        s = set(nums)
        for x in s:
            if x in above:
                continue
            upper = x
            while upper in s:
                upper += 1
            upper -= 1
            lower = x
            while lower in s:
                lower -= 1
            lower += 1

            for y in range(lower, upper + 1):
                below[y] = y - lower
                above[y] = upper - y
        #print(above)
        #print(below)
        max_length = 0
        for x in s:
            max_length = max(max_length, above[x] + below[x] + 1)
        return max_length