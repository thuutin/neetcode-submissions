class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        buffer = [0] * len(nums)
        def sort(i, j):
            if i >= j:
                return
            mid = (i + j) // 2
            sort(i, mid)
            sort(mid + 1, j)
            a = i
            b = mid + 1
            k = 0
            while a <= mid or b <= j:
                if b > j or (a <= mid and nums[a] < nums[b]):
                    buffer[k] = nums[a]
                    a += 1
                else:
                    buffer[k] = nums[b]
                    b += 1
                k += 1
            nums[i:j + 1] = buffer[:k]

        sort(0, len(nums) - 1)
        return nums