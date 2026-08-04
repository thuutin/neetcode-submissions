class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        rev = nums2[::-1]
        def count_product_smaller_equal_than(target):
            c = 0
            for i, x in enumerate(nums1):
                if x < 0:
                    nn2 = rev
                else:
                    nn2 = nums2
                if x * nn2[0] > target:
                    continue
                s = 0
                e = len(nn2) - 1
                while s < e:
                    m = (s + e + 1) // 2
                    if nn2[m] * x <= target:
                        s = m
                    else:
                        e = m - 1
                c += s + 1
            return c
        s1 = [nums1[0], nums1[-1]]
        s2 = [nums2[0], nums2[-1]]
        s = []
        for x in s1:
            for y in s2:
                s.append(x * y)
        start = min(s)
        end = max(s)
        while start < end:
            mid = (start + end) // 2
            if count_product_smaller_equal_than(mid) < k:
                start = mid + 1
            else:
                end = mid
        return start
                