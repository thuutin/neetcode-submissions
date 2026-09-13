class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i, j = 0, len(people) - 1
        c = 0
        people.sort()
        while i <= j:

            if i < j and people[j] + people[i] <= limit:
                i += 1
                j -= 1
                c += 1
            else:
                j -= 1
                c += 1
        return c