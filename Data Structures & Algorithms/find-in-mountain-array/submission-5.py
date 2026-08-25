class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        start = 0
        n = mountainArr.length()
        end = n - 1
        cache = {}
        
        while start < end:
            lower_mid = (start + end) // 2
            upper_mid = lower_mid + 1
            lower = mountainArr.get(lower_mid)
            upper = mountainArr.get(upper_mid)
            cache[lower_mid] = lower
            cache[upper_mid] = upper
            if lower < upper:
                start = upper_mid
            else:
                end = lower_mid
        peak = start
        def search(start, end, increasing):
            while start <= end:
                mid = (start + end) // 2
                value = mountainArr.get(mid)
                if value == target:
                    return mid
                elif (value < target and increasing) or (value > target and not increasing):
                    start = mid + 1
                else:
                    end = mid - 1
                
            return None
        left = search(0, peak, True)
        if left != None:
            return left
        right = search(peak + 1, n - 1, False)
        if right != None:
            return right
        return -1

        
            
