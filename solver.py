import math

class MathEngine:
    @staticmethod
    def prime_factors(n: int) -> dict:
        """Returns prime factorization as a dictionary of {prime: exponent}."""
        factors = {}
        # Count factor 2
        while n % 2 == 0:
            factors[2] = factors.get(2, 0) + 1
            n //= 2
            
        # Check odd factors up to sqrt(n)
        d = 3
        while d * d <= n:
            while n % d == 0:
                factors[d] = factors.get(d, 0) + 1
                n //= d
            d += 2
            
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
            
        return factors

    @staticmethod
    def count_divisors(n: int) -> int:
        """Calculates total positive divisors using prime factorization exponents."""
        factors = MathEngine.prime_factors(n)
        total = 1
        for exp in factors.values():
            total *= (exp + 1)
        return total

    @staticmethod
    def modular_power(base: int, exp: int, mod: int) -> int:
        """Solves (base^exp) % mod using fast exponentiation."""
        return pow(base, exp, mod)

    @staticmethod
    def combinations_count(n: int, r: int) -> int:
        """Computes nCr = n! / (r! * (n - r)!)."""
        if r < 0 or r > n:
            return 0
        return math.comb(n, r)

    @staticmethod
    def permutations_count(n: int, r: int) -> int:
        """Computes nPr = n! / (n - r)!."""
        if r < 0 or r > n:
            return 0
        return math.perm(n, r) 