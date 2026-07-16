def printNaturalNumbers():
    n = int(input("Enter n: "))
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1

def printOddNumbersInRange():
    start, end = map(int, input("Enter start and end: ").split())
    for i in range(start, end + 1):
        if i % 2 != 0: print(i, end=" ")

def printDivisibleBy3Or5():
    start, end = map(int, input("Enter range: ").split())
    i = start
    while i <= end:
        if i % 3 == 0 or i % 5 == 0: print(i, end=" ")
        i += 1

def countEvenOdd():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    even = odd = 0
    for n in nums:
        if n % 2 == 0: even += 1
        else: odd += 1
    print(f"Even: {even}, Odd: {odd}")

def calculateFactorial():
    n = int(input("Enter a number: "))
    fact = 1
    for i in range(1, n + 1): fact *= i
    print(f"Factorial: {fact}")

def checkPrime():
    n = int(input("Enter a number: "))
    is_prime = n > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: is_prime = False; break
    print("Prime" if is_prime else "Not Prime")

def reverseNumber():
    n = int(input("Enter number: "))
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    print(f"Reversed: {rev}")

def sumOfDigits():
    n = int(input("Enter number: "))
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    print(f"Sum: {total}")

def fibonacciSeries():
    n = int(input("Enter limit: "))
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

def checkArmstrong():
    n = int(input("Enter number: "))
    temp = n
    sum_pow = 0
    while temp > 0:
        sum_pow += (temp % 10)**len(str(n))
        temp //= 10
    print("Armstrong" if sum_pow == n else "Not Armstrong")

def checkPalindrome():
    n = input("Enter string/number: ")
    print("Palindrome" if n == n[::-1] else "Not Palindrome")

def checkPerfectNumber():
    n = int(input("Enter number: "))
    div_sum = sum(i for i in range(1, n) if n % i == 0)
    print("Perfect Number" if div_sum == n else "Not Perfect")

def printPrimes1To100():
    for num in range(1, 101):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0: break
            else: print(num, end=" ")
