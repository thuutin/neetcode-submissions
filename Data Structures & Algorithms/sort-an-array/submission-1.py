class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(i, j):
            if i >= j:
                return
            mid = (i + j) // 2
            sort(i, mid)
            sort(mid + 1, j)
            a = i
            b = mid + 1
            arr = []
            while a <= mid or b <= j:
                if b > j or (a <= mid and nums[a] < nums[b]):
                    arr.append(nums[a])
                    a += 1
                else:
                    arr.append(nums[b])
                    b += 1
            nums[i:j + 1] = arr

        sort(0, len(nums) - 1)
        return nums