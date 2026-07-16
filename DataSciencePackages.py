import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def demonstrateNumpy():
    # I. Element-wise addition
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"Addition: {arr1 + arr2}")

    # II. Matrix multiplication
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])
    print(f"Matrix Product:\n {np.dot(mat1, mat2)}")

def demonstrateMatplotlib():
    # III. Line Graph
    x = [1, 2, 3, 4]
    y1 = [1, 4, 9, 16]
    y2 = [1, 2, 3, 4]
    plt.plot(x, y1, label='Square')
    plt.plot(x, y2, label='Linear')
    plt.legend()
    plt.title("Line Graph")
    plt.show()

    # IV. Pie Chart
    labels = ['A', 'B', 'C']
    sizes = [30, 45, 25]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Pie Chart")
    plt.show()

def demonstrateScipy():
    # V. SciPy Statistics
    data = [1, 2, 3, 4, 5, 5, 6]
    print(f"Mean: {np.mean(data)}")
    print(f"Mode: {stats.mode(data, keepdims=True)}")
