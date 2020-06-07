import math

def x_raised_to_y(x, y):
	print('X**y =', x**y)

def log_of_x(x):
	print('log(x) =', math.log2(x))

x = int(input("Enter a number x:"))
y = int(input("Enter a number y:"))
x_raised_to_y(x, y)
log_of_x(x)