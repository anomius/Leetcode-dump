class Solution:
    def countPrimes(self, n: int) -> int:
        if n<= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for x in range(i*i, n, i):
                    is_prime[x] = False

        return len([i for i in range(n) if is_prime[i]])
    
                           
                           