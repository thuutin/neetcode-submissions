class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #[3, 1, 5, 2, 3]
        # 0, 1, 2, 3, 4
        slow = 0
        fast = 0
        slow, fast = nums[slow], nums[nums[fast]]
        while slow != fast:
            # print(slow, fast)
            slow, fast = nums[slow], nums[nums[fast]]
        second = 0
        while second != slow:
            second, slow = nums[second], nums[slow]
        return slow
