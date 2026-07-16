def manageListOperations():
    # I. Create and print
    my_list = [10, 20, 30, 40]
    print(f"List: {my_list}")

    # II. Separate odd and even
    nums = [1, 2, 3, 4, 5, 6]
    even = [x for x in nums if x % 2 == 0]
    odd = [x for x in nums if x % 2 != 0]
    print(f"Even: {even}, Odd: {odd}")

    # III. Search item
    item = 20
    print(f"Found: {item in my_list}")

    # IV. Add and delete
    my_list.append(50)
    my_list.remove(10)
    print(f"Modified List: {my_list}")

def matrixMultiplication():
    # V. 3x3 Matrix Multiplication
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    result = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    for row in result: print(row)

def demonstrateListFunctions():
    # VI. List methods
    l = [3, 1, 2]
    l.sort()
    l.reverse()
    l.pop()
    print(f"Processed List: {l}")

def demonstrateTuples():
    # VII. Tuples
    t = (1, 2, 3)
    print(f"Tuple: {t}, First element: {t[0]}")

def demonstrateStrings():
    # VIII. Strings and functions
    s = "Hello World"
    print(s.upper(), s.lower(), s.replace("World", "Python"))

def printAlphabet():
    # IX. Print A-Z
    import string
    print(list(string.ascii_uppercase))

def checkSubstring():
    # X. Check substring
    main_str = "Brainware University"
    sub = "Brain"
    print(f"Is present: {sub in main_str}")
