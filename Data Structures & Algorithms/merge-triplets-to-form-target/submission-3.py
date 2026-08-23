class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        found = [False] * 3
        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            
            found[0] = found[0] or a == x
            found[1] = found[1] or b == y
            found[2] = found[2] or c == z
        return all(found)