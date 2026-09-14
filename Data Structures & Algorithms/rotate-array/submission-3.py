class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%= n

        def move(start):
            i = start
            c = 0
            x = nums[i]
            while i != start or c == 0:
                x, nums[(i + k) % n ] =  nums[(i + k) % n], x
                i += k
                i %= n
                c += 1
            return c
        cc = 0
        for i in range(k):
            cc += move(i)
            if cc == n:
                break
                