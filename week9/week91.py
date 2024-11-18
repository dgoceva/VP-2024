import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data, bins=10): 
    plt.hist(data, bins=bins)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

def plot_sinx():
    x = np.linspace(0, 2 * np.pi, 100)
    print(x)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Sine Function")
    plt.show()

def f(x):
    return np.sin(x) + np.cos(x)

def f1(x):
    return np.sin(x) + x + x * np.sin(x)

if __name__=="__main__":
    # data = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10, 10]
    # plot_histogram(data)
    # plot_sinx()
    x = np.arange(0,2*np.pi,0.01)
    y = f(x)
    plt.plot(x, y,color="red",label="sin(x)+cos(x)")
    y = f1(x)
    plt.plot(x, y,color="blue",label="sin(x)+x+x*sin(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="upper left")
    plt.title("User defined functions")
    plt.show()