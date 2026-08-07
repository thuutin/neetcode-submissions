class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x
        diff_bit = 0 
        for i in range(32):
            if (xor >> i) & 1 == 1:
                diff_bit = i
                break

        a = 0
        b = 0
        for x in nums:
            if (x >> diff_bit) & 1 == 1:
                a ^= x
            else:
                b ^= x
        return [a, b]