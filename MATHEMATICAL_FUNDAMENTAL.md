# Mathematical Fundamentals for Competitive Programming

The essential math toolkit for Codeforces. Every formula here appears repeatedly in problems—master these and you'll recognize patterns instantly.

---

## 1. Basic Arithmetic & Algebra

### Sum formulas
```
Sum of 1 to n:        n(n+1)/2
Sum of squares:       n(n+1)(2n+1)/6
Sum of cubes:         [n(n+1)/2]²
Sum of odd numbers:   n²  (1+3+5+...+(2n-1))
Sum of even numbers:  n(n+1)
```

### Arithmetic progression (AP)
```
nth term:     aₙ = a₁ + (n-1)d
Sum of n terms: Sₙ = n/2 × (2a₁ + (n-1)d) = n/2 × (a₁ + aₙ)
```

### Geometric progression (GP)
```
nth term:     aₙ = a₁ × r^(n-1)
Sum of n terms: Sₙ = a₁(rⁿ - 1)/(r - 1)   [r ≠ 1]
Infinite sum:  S∞ = a₁/(1 - r)              [|r| < 1]
```

### Quadratic formula
```
ax² + bx + c = 0
x = (-b ± √(b² - 4ac)) / 2a
Discriminant D = b² - 4ac
  D > 0: two real roots
  D = 0: one real root
  D < 0: no real roots
```

### Important algebraic identities
```
(a + b)² = a² + 2ab + b²
(a - b)² = a² - 2ab + b²
a² - b² = (a + b)(a - b)
(a + b)³ = a³ + 3a²b + 3ab² + b³
a³ + b³ = (a + b)(a² - ab + b²)
a³ - b³ = (a - b)(a² + ab + b²)
(a + b + c)² = a² + b² + c² + 2(ab + bc + ca)
```

### AM-GM inequality
```
(a₁ + a₂ + ... + aₙ)/n ≥ ⁿ√(a₁a₂...aₙ)
Equality when all aᵢ are equal.
```

---

## 2. Divisibility & Modular Arithmetic

### Divisibility rules
```
By 2:  last digit even
By 3:  sum of digits divisible by 3
By 4:  last two digits divisible by 4
By 5:  last digit is 0 or 5
By 6:  divisible by both 2 and 3
By 8:  last three digits divisible by 8
By 9:  sum of digits divisible by 9
By 11: alternating sum of digits divisible by 11
```

### Modular arithmetic rules
```
(a + b) mod m = ((a mod m) + (b mod m)) mod m
(a - b) mod m = ((a mod m) - (b mod m) + m) mod m
(a × b) mod m = ((a mod m) × (b mod m)) mod m
(a / b) mod m = (a × b⁻¹) mod m   [b⁻¹ = modular inverse]
```

### Fast modular exponentiation
```python
def power(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result

# Python built-in (faster):
pow(base, exp, mod)
```

### Modular inverse
```
If gcd(a, m) = 1, then a⁻¹ exists.
Fermat's little theorem (m prime): a⁻¹ ≡ a^(m-2) mod m
Extended Euclidean: find x such that ax + my = 1, then a⁻¹ = x
```

```python
# Fermat (m prime)
inv = pow(a, m - 2, m)

# Extended Euclidean (any coprime m)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def mod_inv(a, m):
    g, x, _ = extended_gcd(a, m)
    return x % m if g == 1 else None
```

### Chinese Remainder Theorem (CRT)
For coprime moduli m₁, m₂, ..., mₖ:
```
x ≡ r₁ (mod m₁)
x ≡ r₂ (mod m₂)
...
x ≡ rₖ (mod mₖ)
```
Has a unique solution modulo M = m₁ × m₂ × ... × mₖ.

### Ceiling division
```python
(a + b - 1) // b   # ceil(a / b) for positive integers
```

---

## 3. GCD & LCM

### Definitions
```
gcd(a, b) = largest positive integer dividing both a and b
lcm(a, b) = smallest positive integer divisible by both a and b
```

### Fundamental relation
```
gcd(a, b) × lcm(a, b) = a × b
lcm(a, b) = a × b / gcd(a, b)
```

### Euclidean algorithm
```python
import math
math.gcd(a, b)          # built-in (fast, C implementation)
math.gcd(*arr)          # Python 3.9+ for multiple args
from functools import reduce
reduce(math.gcd, arr)   # GCD of array
```

### Extended Euclidean algorithm
Finds x, y such that `ax + by = gcd(a, b)`.
```python
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y
```

### Properties
```
gcd(a, 0) = a
gcd(a, b) = gcd(b, a mod b)
gcd(a, b) = gcd(a - b, b)
gcd(ka, kb) = k × gcd(a, b)
gcd(a, b) = 1  →  a and b are coprime
```

### LCM of array (watch for overflow)
```python
from functools import reduce
import math
def lcm(a, b):
    return a // math.gcd(a, b) * b  # divide first to avoid overflow

reduce(lcm, arr)
```

---

## 4. Prime Numbers

### Fundamental theorem of arithmetic
Every integer n > 1 can be uniquely written as:
```
n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ
```
where pᵢ are distinct primes.

### Number of divisors
If n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ, then:
```
d(n) = (a₁ + 1)(a₂ + 1)...(aₖ + 1)
```

### Sum of divisors
```
σ(n) = [(p₁^(a₁+1) - 1)/(p₁ - 1)] × [(p₂^(a₂+1) - 1)/(p₂ - 1)] × ...
```

### Euler's totient function φ(n)
Counts integers 1 ≤ k ≤ n with gcd(k, n) = 1.
```
φ(n) = n × (1 - 1/p₁) × (1 - 1/p₂) × ... × (1 - 1/pₖ)
φ(p) = p - 1  for prime p
φ(p^k) = p^k - p^(k-1)
```

### Sieve of Eratosthenes
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

# Time: O(n log log n), Space: O(n)
```

### Linear sieve (smallest prime factor)
```python
def linear_sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

# Factorize n in O(log n):
def factorize(n, spf):
    factors = []
    while n > 1:
        p = spf[n]
        cnt = 0
        while n % p == 0:
            n //= p
            cnt += 1
        factors.append((p, cnt))
    return factors
```

### Prime factorization (trial division)
```python
def factorize(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Time: O(√n)
```

### Check primality
```python
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

### Number of primes up to n
```
π(n) ≈ n / ln(n)   (prime number theorem)
π(10⁶) = 78,498
π(10⁷) = 664,579
```

---

## 5. Combinatorics

### Factorial
```
n! = 1 × 2 × 3 × ... × n
0! = 1
n! ≈ √(2πn) × (n/e)ⁿ   (Stirling's approximation)
```

### Permutations
```
P(n, r) = n! / (n - r)!     (ordered selection of r from n)
P(n, n) = n!
```

### Combinations
```
C(n, r) = n! / (r!(n - r)!)     (unordered selection)
C(n, r) = C(n, n - r)
C(n, 0) = C(n, n) = 1
C(n, 1) = n
```

### Pascal's identity
```
C(n, r) = C(n-1, r-1) + C(n-1, r)
```

### Key combinatorial identities
```
C(n, 0) + C(n, 1) + ... + C(n, n) = 2ⁿ
C(n, 0) - C(n, 1) + C(n, 2) - ... = 0
C(n, 0) + C(n, 2) + C(n, 4) + ... = 2^(n-1)
C(n, 1) + C(n, 3) + C(n, 5) + ... = 2^(n-1)
C(n, r) × C(r, k) = C(n, k) × C(n-k, r-k)
Hockey stick: C(k, k) + C(k+1, k) + ... + C(n, k) = C(n+1, k+1)
```

### Stars and bars
Number of ways to distribute n identical objects into k distinct bins:
```
C(n + k - 1, k - 1)
```

### Catalan numbers
```
Cₙ = C(2n, n) / (n + 1)
C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42
```

Applications: valid parentheses, binary trees, polygon triangulations.

### Derangements
Number of permutations with no fixed points:
```
D(n) = n! × Σ(k=0 to n) (-1)^k / k!
D(n) = (n-1)(D(n-1) + D(n-2))
D(0) = 1, D(1) = 0, D(2) = 1, D(3) = 2, D(4) = 9
```

### Precompute factorials and inverse factorials
```python
MOD = 10**9 + 7
MAXN = 2 * 10**5 + 5

fact = [1] * MAXN
inv_fact = [1] * MAXN

for i in range(1, MAXN):
    fact[i] = fact[i-1] * i % MOD

inv_fact[MAXN-1] = pow(fact[MAXN-1], MOD-2, MOD)
for i in range(MAXN-2, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD
```

---

## 6. Number Systems & Bases

### Binary representation
```python
bin(n)         # '0b1010'
bin(n)[2:]     # '1010'
int('1010', 2) # 10
```

### Decimal to any base
```python
def to_base(n, b):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = []
    while n > 0:
        result.append(digits[n % b])
        n //= b
    return ''.join(reversed(result))
```

### Any base to decimal
```python
def to_decimal(s, b):
    result = 0
    for c in s:
        result = result * b + int(c, 36)  # handles 0-9, A-Z
    return result
```

### Key binary facts
```
n has ⌊log₂(n)⌋ + 1 bits
n & (n-1) = 0  ⟺  n is a power of 2
n & (-n) isolates the lowest set bit
n >> k = n // 2^k
n << k = n × 2^k
XOR of 1 to n follows a pattern mod 4:
  n % 4 == 0 → n
  n % 4 == 1 → 1
  n % 4 == 2 → n + 1
  n % 4 == 3 → 0
```

---

## 7. Sequences & Series

### Fibonacci
```
F₀ = 0, F₁ = 1
Fₙ = Fₙ₋₁ + Fₙ₋₂
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```
- Binet's formula: `Fₙ = (φⁿ - ψⁿ) / √5` where `φ = (1+√5)/2`, `ψ = (1-√5)/2`
- GCD property: `gcd(Fₘ, Fₙ) = F_gcd(m,n)`
- Sum: `F₁ + F₂ + ... + Fₙ = Fₙ₊₂ - 1`
- Cassini's identity: `Fₙ₋₁ × Fₙ₊₁ - Fₙ² = (-1)ⁿ`

### Triangular numbers
```
Tₙ = n(n+1)/2
1, 3, 6, 10, 15, 21, 28, ...
Check: 8Tₙ + 1 is a perfect square
```

### Perfect squares
```
1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...
Number of squares ≤ n: ⌊√n⌋
```

### Powers of 2
```
2⁰=1, 2¹=2, 2²=4, 2³=8, 2⁴=16, 2⁵=32, 2⁶=64, 2⁷=128,
2⁸=256, 2⁹=512, 2¹⁰=1024, 2¹⁶=65536, 2²⁰≈10⁶,
2³⁰≈10⁹, 2³²≈4.3×10⁹, 2⁶³≈9.2×10¹⁸
```
Useful: `2¹⁰ ≈ 10³`, so `2³⁰ ≈ 10⁹`.

---

## 8. Factorials & Large Numbers

```
10!  = 3,628,800
12!  = 479,001,600
13!  = 6,227,020,800          (> 32-bit int max)
20!  = 2,432,902,008,176,640,000
21!  > 64-bit unsigned int max
```

- **Trailing zeros in n!**: `⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...`
- **Legendre's formula** for exponent of prime p in n!: `⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + ...`

```python
def trailing_zeros(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
```

---

## 9. Probability & Expected Value

### Basic probability
```
P(A) = favorable outcomes / total outcomes
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
P(A ∩ B) = P(A) × P(B|A)       (conditional)
P(complement) = 1 - P(A)
```

### Expected value
```
E[X] = Σ xᵢ × P(X = xᵢ)
Linearity of expectation: E[X + Y] = E[X] + E[Y]  (always, even if dependent)
```

### Birthday paradox
With n people, probability of at least one shared birthday:
```
P ≈ 1 - e^(-n²/2M)   where M = 365
```

---

## 10. Coordinate Geometry

### Distance formulas
```
Euclidean:   √((x₂-x₁)² + (y₂-y₁)²)
Manhattan:   |x₂-x₁| + |y₂-y₁|
Chebyshev:   max(|x₂-x₁|, |y₂-y₁|)
```

### Line through two points
```
Slope:       m = (y₂-y₁)/(x₂-x₁)
Equation:    y - y₁ = m(x - x₁)
General:     ax + by + c = 0  where a = y₁-y₂, b = x₂-x₁, c = x₁y₂ - x₂y₁
```

### Area of triangle (shoelace formula)
```
Area = |x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| / 2
```

### Area of polygon (shoelace)
```
Area = |Σ(xᵢ × yᵢ₊₁ - xᵢ₊₁ × yᵢ)| / 2
```

### Point in polygon (ray casting)
```python
def point_in_polygon(px, py, poly):
    n = len(poly)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > py) != (yj > py)) and (px < (xj - xi) * (py - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside
```

### Circle
```
Area:        πr²
Circumference: 2πr
Equation:    (x - h)² + (y - k)² = r²
```

### Key constants
```
π ≈ 3.14159265358979
e ≈ 2.71828182845905
φ = (1+√5)/2 ≈ 1.61803398874989   (golden ratio)
```

---

## 11. Trigonometry (Less Common but Useful)

```
sin²θ + cos²θ = 1
sin(2θ) = 2sinθcosθ
cos(2θ) = cos²θ - sin²θ = 1 - 2sin²θ = 2cos²θ - 1
tan(2θ) = 2tanθ / (1 - tan²θ)
sin(A+B) = sinAcosB + cosAsinB
cos(A+B) = cosAcosB - sinAsinB
Law of sines:   a/sinA = b/sinB = c/sinC = 2R
Law of cosines: c² = a² + b² - 2ab·cosC
```

---

## 12. Inequalities & Bounds

### Useful inequalities
```
AM-GM:    (a+b)/2 ≥ √(ab)
Cauchy-Schwarz: (Σaᵢbᵢ)² ≤ (Σaᵢ²)(Σbᵢ²)
Triangle: a + b > c for sides of a triangle
Bernoulli: (1 + x)ⁿ ≥ 1 + nx  for x ≥ -1, n ≥ 1
```

### Common bounds used in solutions
```
2^n grows exponentially — feasible only for n ≤ 20–25
n! grows factorially — feasible only for n ≤ 10–12
n log n is fast up to n = 10⁶–10⁷
√n up to n = 10¹⁸ is feasible
n² is fast up to n ≈ 5000–10000
n³ is fast up to n ≈ 300–500
```

### Harmonic sum
```
H(n) = 1 + 1/2 + 1/3 + ... + 1/n ≈ ln(n) + γ
γ ≈ 0.5772156649  (Euler-Mascheroni constant)

Sum of n/i for i=1..n = n × H(n) ≈ n ln(n)
Useful: Σ ⌊n/i⌋ = O(n log n)
```

---

## 13. Frequently Used Constants & Values

```
MOD1 = 10⁹ + 7      (most common)
MOD2 = 10⁹ + 9
MOD3 = 998244353    (NTT-friendly)
INF  = 10¹⁸         (for "infinity" in Dijkstra)
NEG_INF = -10¹⁸
EPS  = 10⁻⁹         (float comparison)
```

### Float comparison
```python
def is_equal(a, b, eps=1e-9):
    return abs(a - b) < eps

def is_zero(x, eps=1e-9):
    return abs(x) < eps
```

---

## 14. Number Theory Functions Summary

| Function | Formula / Method | Complexity |
|----------|-----------------|------------|
| gcd(a, b) | Euclidean algorithm | O(log min(a,b)) |
| lcm(a, b) | a×b/gcd(a,b) | O(log min(a,b)) |
| φ(n) | Euler's totient | O(√n) per query |
| d(n) — divisors | prime factorization | O(√n) per query |
| σ(n) — sum divisors | prime factorization | O(√n) per query |
| is_prime(n) | trial division | O(√n) |
| Sieve | Eratosthenes | O(n log log n) |
| Fast power | binary exponentiation | O(log n) |
| Modular inverse | Fermat / extended Euclid | O(log MOD) |
| nCr | factorials + inverse | O(1) after O(n) precompute |

---

## 15. Quick Reference: Which Formula to Use

| Problem asks | Use |
|-------------|-----|
| Sum 1..n | n(n+1)/2 |
| Count divisors | Prime factorization + (aᵢ+1) product |
| GCD of array | `reduce(math.gcd, arr)` |
| LCM of array | `reduce(lambda a,b: a//gcd(a,b)*b, arr)` |
| nCr mod p | Precompute factorials + inverse factorials |
| Is n prime? | Trial division to √n |
| All primes ≤ n | Sieve |
| Factorize n | Trial division to √n, or SPF sieve |
| Modular inverse | `pow(a, p-2, p)` for prime p |
| Trailing zeros in n! | `n//5 + n//25 + n//125 + ...` |
| Catalan number | C(2n,n)/(n+1) |
| Number of ways to distribute | Stars and bars: C(n+k-1, k-1) |
| Distance between points | Euclidean / Manhattan / Chebyshev |
| Area of polygon | Shoelace formula |

---

## 16. Common Pitfalls

1. **Integer division**: `a / b` in Python 3 gives float. Use `a // b` for integer division.
2. **Negative modulo**: `-7 % 3` in Python gives `2` (correct), but in C++ gives `-1`. Be aware when porting.
3. **Overflow**: Python has arbitrary precision, so no overflow—but it's slower for very large numbers.
4. **LCM overflow**: Compute `a // gcd(a,b) * b` (divide first), not `a * b // gcd(a,b)`.
5. **Modular inverse exists only if gcd(a, m) = 1**.
6. **Fermat's little theorem requires prime modulus**.
7. **Float precision**: Never compare floats with `==`. Use `abs(a-b) < 1e-9`.
8. **Sieve size**: For n = 10⁷, a boolean list uses ~10 MB in Python—watch memory limits.
9. **Recursion depth**: Python's default is ~1000. Use `sys.setrecursionlimit(10**6)` for deep recursion.
10. **`pow(a, b)` vs `pow(a, b, m)`**: The three-argument version is modular and much faster for large exponents.

---

## 17. The Math You Actually Need by Rating

| Rating | Math Topics |
|--------|-------------|
| 800–1000 | Basic arithmetic, parity, divisibility, simple formulas |
| 1100–1300 | GCD/LCM, primes, modular arithmetic, combinatorics basics |
| 1400–1600 | Sieve, factorization, nCr with modular inverse, AP/GP |
| 1600–1800 | Euler's totient, CRT, Catalan, expected value |
| 1800–2000 | Advanced combinatorics, probability, number theory functions |
| 2000+ | Everything + game theory math, generating functions |

---

*Master the first 8 sections thoroughly—they cover 90% of what Codeforces throws at you. The remaining sections are reference material to consult when a specific problem demands them.*