class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split_with_max_sum(maxSum):
            s = 0
            count = 0
            for x in nums:
                if s + x <= maxSum:
                    s += x
                elif x > maxSum:
                    return False
                else:
                    count += 1
                    s = x
            if s > 0:
                count += 1
            return count <= k

        start = min(nums)
        end = sum(nums)
        while start < end:
            mid = (start + end) // 2
            #print(mid, split_with_max_sum(mid))
            if split_with_max_sum(mid):
                end = mid
            else:
                start = mid + 1
        return start