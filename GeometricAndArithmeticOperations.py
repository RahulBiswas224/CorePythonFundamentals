import math

def calculateShapesArea():
    side = float(input("Enter side of the square: "))
    print(f"Area of Square: {side**2}")
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    print(f"Area of Rectangle: {length * width}")

def calculateCircleProperties():
    radius = float(input("Enter radius of circle: "))
    print(f"Area: {math.pi * radius**2}")
    print(f"Circumference: {2 * math.pi * radius}")

def swapWithTemp():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    temp = a
    a = b
    b = temp
    print(f"Swapped: a={a}, b={b}")

def swapWithoutTemp():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    a, b = b, a
    print(f"Swapped: a={a}, b={b}")

def convertDaysToTime():
    total_days = int(input("Enter total days: "))
    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30
    print(f"{years} Years, {months} Months, {days} Days")

def calculateSalary():
    basic = float(input("Enter Basic Salary: "))
    da = 0.20 * basic
    ta = 0.05 * basic
    hra = 0.10 * basic
    print(f"Cash in hand: {basic + da + ta + hra}")

def calculateCylinderVolume():
    r = float(input("Radius: "))
    h = float(input("Height: "))
    print(f"Volume: {math.pi * (r**2) * h}")

def convertHeight():
    cm = float(input("Height in cm: "))
    inches = cm / 2.54
    feet = inches // 12
    remaining_inches = inches % 12
    print(f"{int(feet)} feet and {round(remaining_inches, 2)} inches")

def reverseTwoDigits():
    num = int(input("Enter a 2-digit number: "))
    print(f"Reversed: {(num % 10) * 10 + (num // 10)}")

def calculateCompoundInterest():
    p = float(input("Principal: "))
    t = float(input("Time (years): "))
    r = float(input("Rate: "))
    amount = p * (pow((1 + r / 100), t))
    print(f"Amount: {amount}, Interest: {amount - p}")

def calculateMean():
    vals = [float(x) for x in input("Enter numbers separated by space: ").split()]
    print(f"Mean: {sum(vals) / len(vals)}")
