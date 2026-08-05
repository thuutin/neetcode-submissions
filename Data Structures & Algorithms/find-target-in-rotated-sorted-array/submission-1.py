class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            rotated = nums[l] > nums[r]
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if not rotated:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target == nums[l]:
                    return l
                if target == nums[r]:
                    return r
                if nums[mid] >= nums[l]:
                    if target > nums[mid]:
                        l = mid + 1
                    elif target > nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if target < nums[mid]:
                        r = mid- 1
                    elif target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1
            print(rotated, l, r)
        return -1