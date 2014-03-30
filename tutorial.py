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

# In Python, the in operator can be used to test if an element is present in a list.
x =  [1, 2, 3, 4]
print 3 in x
print 9 in x
print 7 not in x

# Replacing placeholders in a string with values is very useful operation. In Python, this is done using string formatting operator %. Here is an example demonstrating it.
 # In the below example, %d is a placeholder that expects an integer and %s is a placeholder that expects a string.
num = 0
title = "String Basics"
print 'Lesson %d: %s' % (num, title)

#return unique values in list
def unique(values):
    """Finds all unique elements of a list.

        >>> unique([])
        []
        >>> unique([1, 2, 1])
        [1, 2]
        >>> unique([1, 2, 1, 3, 4, 2])
        [1, 2, 3, 4]
    """
    # your code here
    newList = list(set(values))
    return newList

# sort on lower case
def lower(s):
    return s.lower()

def isort(names):
    """Sorts a list of strings ignoring the case.

        >>> isort(['alice', 'dave', 'BOB','charlie']
        ['alice', 'BOB', 'charlie', 'dave']
    """
    # Forcing all sort comparisons to be in lowercase, by passing key=lower
    return sorted(names, key=lower)

