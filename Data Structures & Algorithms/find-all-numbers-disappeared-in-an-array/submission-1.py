class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        print(nums)
        e = 1
        i = 0
        while i < n:
            x = nums[i]
            if x < e:
                i += 1
            elif x == e:
                e += 1
                i += 1
            else:
                res.append(e)
                e += 1
        while e <= n:
            res.append(e)
            e += 1
        return res