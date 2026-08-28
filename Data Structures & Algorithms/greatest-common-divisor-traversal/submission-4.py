class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        primes = []
        MAX = max(nums)
        not_prime = [False] * (MAX + 1) 
        not_prime[0] = True
        not_prime[1] = True
        for x in range(2, MAX + 1):
            if not_prime[x]:
                continue
            m = 2 * x
            while m <= MAX:
                not_prime[m] = True
                m += x
        for i in range(len(not_prime)):
            if not not_prime[i]:
                primes.append(i)
            
        groups = defaultdict(list)
        for p in primes:
            for i, x in enumerate(nums):
                if x % p == 0:
                    groups[p].append(i)
                    
        root = list(range(len(nums)))
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]
        
        def union(i, j):
            rooti = find(i)
            rootj = find(j)
            if rooti == rootj:
                return False
            root[rooti] = rootj

        for p, numbers in groups.items():
            for i in range(1, len(numbers)):
                union(numbers[0], numbers[i])
        #print(root)
        #print(groups)
        for i in range(len(nums) - 1):
            if find(i) != find(i + 1):
                return False
        
        return True


