class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        pass


        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
        
        res = [-1, -1]
        min_diff = float('inf')
        l, r = left, left + 1

        if l == 1:
            l += 1
            r += 1

        while r <= right:
            
            if is_prime[l] and is_prime[r]:
                if r - l < min_diff:
                    min_diff = r - l
                    res = [l, r]
                
                l = r
            if not is_prime[l]:
                l = r
            
            r += 1
        
        return res

        
