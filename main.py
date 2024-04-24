import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
def function(x,func):
    y = eval(func)
    #y=-x**3+3*x**2-2
    return(y)
def left(a,b,dx,area,n,func):
    fig, ax = plt.subplots()
    for i in range(n):
        x = a + i * dx  # x limit on the left side of the rectangle
        fx = function(x,func)  # f(x) value of x with the function above
        rect = Rectangle((x, 0), dx, fx, linewidth=1, edgecolor='blue', facecolor='lightblue')
        # plot the rectangle   (x,y),lenth,height, styles
        area += fx * dx
        ax.add_patch(rect)
    title='riemann sum',area
    x_values = np.linspace(-10, 10, 20)
    y_values = function(x_values,func)
    plt.plot(x_values, y_values, 'r-', label='Function ')  # polynomial function  x, y, color, label
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
    print(area)
def right(a,b,dx,area,n,func):
    fig, ax = plt.subplots()
    for i in range(n):
        x = a + i * dx  # x limit on the left side of the rectangle
        w = a + (i + 1) * dx  # limit on the right side of the rectangle
        fw = function(w,func)  # f(w) vaule of w with function abGove
        rect = Rectangle((x, 0), dx, fw, linewidth=1, edgecolor='blue',facecolor='lightblue')  # plot the rectangle
        area +=  fw * dx
        ax.add_patch(rect)
    title = ("Reminsum ", area)
    x_values = np.linspace(-10, 10, 20)
    y_values = function(x_values,func)
    plt.plot(x_values, y_values, 'r-', label='Function ')  # polynomial function
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
    print(area)

def midpoint(a,b,dx,area,n,func):

    fig, ax = plt.subplots()
    for i in range(n):
        x = a + i * dx  # x limit on the left side of the rectangle
        w = a + (i + 1) * dx  # limit on the right side of the rectangle
        fx = function((x + w) / 2,func)  # f(x) value of x with the function above
        rect = Rectangle((x, 0), dx, fx, linewidth=1, edgecolor='blue', facecolor='lightblue')
        area=dx*fx
        ax.add_patch(rect)

    title = ("Reminsum ", area)
    x_values = np.linspace(-10, 10, 20)
    y_values = function(x_values)
    plt.plot(x_values, y_values, 'r-', label='Function')  # polynomial function
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def trapezoids(a,b,dx,area,n,func):
    fig, ax = plt.subplots()
    for i in range(n):
        x = a + i * dx  # x limit on the left side of the rectangle
        w = a + (i + 1) * dx  # limit on the right side of the rectangle
        fx = function(x,func)  # f(x) value of x with the function above
        fw = function(w,func)  # f(w) vaule of w with function above
        vertices = np.array([[x, 0], [x, fx], [w, fw], [w, 0]])
        trapezoid = Polygon(vertices, linewidth=1, edgecolor='blue', facecolor='lightblue')
        ax.add_patch(trapezoid)
        area += (fx + fw) * dx * .5

    print(area)
    title = ("Riemann sum ", area)
    x_values = np.linspace(-10, 10, 20)
    y_values = function(x_values,func)
    plt.plot(x_values, y_values, 'r-', label='Function ')  # polynomial function  x, y, color, label
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
    print(area)

def main():
    func=input("polynomial")
    n=int(input("number of rectangles"))
    inp=input("left,right,midpoint,trapezoids")
    a = -10  # min number on graph for x
    b = 10  # max number on graph of x
    dx = (b - a) / n  # delta x , length of each rectangle
    area = 0
    if inp =="left":
        left(a,b,dx,area,n,func)
    if inp =="right":
        right(a,b,dx,area,n,func)
    if inp =="midpoint":
        midpoint(a, b, dx, area, n,func)
    if inp =="trapezoids":
        trapezoids(a, b, dx, area, n,func)
if __name__ == "__main__":
    main()
