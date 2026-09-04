class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        def intersection(first, second):
            if first[0] > second[0]:
                first, second = second, first
            if second[0] <= first[1]:
                return (second[0], min(first[1], second[1]) )
            return None
        for first in firstList:
            for second in secondList:
                inter = intersection(first, second)
                if inter:
                    intersections.append(inter)                
        return intersections