# Not only that, functions can be passed as argument to another function.

def fxy(f, x, y):
    return f(x) + f(y)

def square(x):
    return x*x

print fxy(square, 3, 4)

# The range function, when called with 2 arguments begin and end, it
#  returns a list containing numbers from begin to end-1. Try creating a list
#  of numbers from 3 to 7 using the range function.

print range(3,8)