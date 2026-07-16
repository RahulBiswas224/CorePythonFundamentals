import math
def checkPrime(n): return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
def checkPalindrome(n): return str(n) == str(n)[::-1]
def calculateFactorial(n): return 1 if n == 0 else n * calculateFactorial(n-1)
def fibonacciSeries(n):
    a, b = 0, 1
    for _ in range(n): print(a, end=" "); a, b = b, a + b
def swapByValue(a, b): return b, a
def findGcdLcm(a, b): return math.gcd(a, b), abs(a * b) // math.gcd(a, b)
