class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split_with_max_sum(maxSum):
            s = 0
            count = 0
            for x in nums:
                if s + x <= maxSum:
                    s += x
                else:
                    count += 1
                    s = x
                    if count > k:
                        return False
            if s > 0:
                count += 1
            return count <= k

        start = max(nums)
        end = sum(sorted(nums)[k-1:])
        while start < end:
            mid = (start + end) // 2
            if split_with_max_sum(mid):
                end = mid
            else:
                start = mid + 1
        return start