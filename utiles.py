import pygame
from math import *
import numpy as np
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP

WIDTH = 600
HEIGHT = 600
CLOCK_TICK = 120

back_ground = (255,255,255)
drawing_color = (0,0,0)
axis_color = (100,100,255)
x_axis_scale = 40
y_axis_scale = 40
def substitute(function_str,numer_to_be_sub):
    returned_str = ""
    for char in function_str:
        if char is "X":
            returned_str += f"({numer_to_be_sub/x_axis_scale})"
        else:
            returned_str += char
    return f"({returned_str}) * {y_axis_scale}"

def line_space_to_draw(function_to_calc_y_axis,surface,center_x,center_y, color = (0,0,0)):
    x_axis = np.linspace(-center_x-1,WIDTH - center_x,WIDTH)
    xi = x_axis[0] + center_x
    yi = eval(substitute(function_to_calc_y_axis,x_axis[0]))
    for x in  np.nditer(x_axis):
        x0 = x + center_x
        y = eval(substitute(function_to_calc_y_axis,x))
        y0 = -y + center_y
        pygame.draw.line(surface,color,(xi,yi),(x0,y0),3)
        xi = x0
        yi = y0


def linear_regression(points, m, c, learning_rate):
    if points == []:
        return [0,0]
    array = np.array(points)
    x = array[:,0]
    y = array[:,1]
    n = len(y)
    y_predicted = m * x + c
    square_error = sum( (y - y_predicted)**2)
    mean_square_error = (1/n) * (square_error)
    slop_grad = (-2/n) * sum( x * (y - y_predicted))
    intercepted_grad = (-2/n) * sum( (y - y_predicted))
    m = m - learning_rate * slop_grad
    c = c - intercepted_grad * learning_rate
    return [m,c,mean_square_error]

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(points, m,c, learning_rate):
    dj_dc = 0
    dj_dw = 0
    n = len(points)
    error = 0
    for point in points:
        z = c + m * point[0]
        y_pred = sigmoid(z)
        error += -(point[1] * np.log(y_pred) + (1 - point[1]) * np.log(1 - y_pred))
        dj_dc += y_pred - point[1]
        dj_dw += (y_pred - point[1]) * point[0]
    error/=n
    dj_dc /= n
    dj_dw /= n
    c -= dj_dc * learning_rate
    m -= dj_dw * learning_rate
    return m,c,  error

def unit_step(value):
    if value>0:
        return 1
    return 0


if __name__ == "__main__":
    m,c = 0,0
    for i in range(1000):
        m,c,e = logistic_regression([[-10,1],[-9,1],[-8,1],[-7,1],[0,0],[1,0],[2,0],[3,0]],m,c,0.01)
        print(e)
    data=-10
    print(round(sigmoid(data*m+c),3))

