def checkEvenOdd():
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")

def checkDivisibleBy2And3():
    num = int(input("Enter a number: "))
    print("Divisible by 2 and 3" if num % 2 == 0 and num % 3 == 0 else "Not divisible")

def checkDivisibleBy3Or5():
    num = int(input("Enter a number: "))
    print("Divisible by 3 or 5" if num % 3 == 0 or num % 5 == 0 else "Not divisible")

def findGreatestOfThree():
    a, b, c = map(int, input("Enter three numbers separated by space: ").split())
    print(f"Greatest: {max(a, b, c)}")

def checkLeapYear():
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def calculateElectricBill():
    units = float(input("Enter units consumed: "))
    if units <= 100: bill = units * 5
    elif units <= 200: bill = units * 7
    elif units <= 300: bill = units * 10
    else: bill = units * 15
    print(f"Total Bill: {bill}")

def calculateGrade():
    perc = float(input("Enter percentage: "))
    if perc > 85: print("Grade: A")
    elif perc >= 75: print("Grade: B")
    elif perc >= 50: print("Grade: C")
    elif perc > 30: print("Grade: D")
    else: print("Fail")

def checkVowelOrConsonant():
    char = input("Enter an alphabet: ").lower()
    if char in 'aeiou': print("Vowel")
    else: print("Consonant")

def checkCharType():
    char = input("Enter a character: ")
    if char.isalpha(): print("Alphabet")
    elif char.isdigit(): print("Digit")
    else: print("Special Character")

def checkCase():
    char = input("Enter a character: ")
    if char.isupper(): print("Uppercase")
    elif char.islower(): print("Lowercase")
    else: print("Not an alphabet")
