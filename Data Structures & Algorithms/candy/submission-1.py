class Solution:
    def candy(self, ratings: List[int]) -> int:
        minIndex = 0
        for i in range(len(ratings)):
            if ratings[i] < ratings[minIndex]:
                minIndex = i
        candy = [1] * len(ratings)
        for i in range(1, len(candy)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = max(candy[i], candy[i - 1] + 1)
        
        for j in range(len(candy) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candy[j] = max(candy[j], candy[j + 1] + 1)
        return sum(candy)