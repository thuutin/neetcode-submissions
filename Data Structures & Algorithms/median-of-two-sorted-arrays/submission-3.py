class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        s1 = len(nums1)
        s2 = len(nums2)
        half = (s1 + s2) // 2
        l1 = 0
        r1 = s1
        while l1 <= r1:
            mid = (l1 + r1) // 2
            other = half - mid
            if mid >= 1 and nums1[mid - 1] > nums2[other]:
                r1 = mid - 1
            elif other >= 1 and mid < s1 and nums2[other - 1] > nums1[mid]:
                l1 = mid + 1
            else:
                if (s1 + s2) % 2 == 0:
                    r = []
                    l = []
                    if mid >= 1:
                        l.append(nums1[mid-1])
                    if other >= 1:
                        l.append(nums2[other - 1])
                    if mid < s1:
                        r.append(nums1[mid])
                    if other < s2:
                        r.append(nums2[other])
                    return (max(l) + min(r)) / 2
                else:
                    r = []
                    if mid < s1:
                        r.append(nums1[mid])
                    if other < s2:
                        r.append(nums2[other])
                    return min(r)
        return None