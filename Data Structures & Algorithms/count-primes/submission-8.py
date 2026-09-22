class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        r = 0
        x = 2
        for x in range(2, n):
            if primes[x]:
                r += 1
                k = 2
                while k * x < n:
                    primes[k *x] = False
                    k += 1
        # print(r)
        return r