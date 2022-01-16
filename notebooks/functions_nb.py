# %%

####  link to refgerence - https://writersbyte.com/featured-post/primer-on-functions-in-python/


# Asserting Arguments
'''
Assert statements are conditional statements but unlike traditional conditions, 
they halt program execution if the condition evaluates as ‘False’. Adding asserts are optional
but they are great for debugging
'''


def sum(i1:int, i2:int):
    assert type(i1) == int and type(i2) == int
    output = i1 + i2
    return output


# %%
# Default Arguments
'''
in certain cases, you might want some arguments to be automatically set a defined default value if not specified

Default arguments in functions are initialized when the function is defined and not when the function is executed. 
If mutable default arguments, such as dictionaries, lists, etc., are modified during the function call, 
they’ll retain that modification in the next call too
'''

def greeting(name:str="User"):
    assert type(name) == str
    print("Hello {}!".format(name))
    print(f"Hello {name}! you are formatted shortly")


# %%
# Variable number of Arguments

# *args
'''
The *args keyword allows the function to receive an arbitrary number of variable type arguments
'''
from functools import reduce

def addmul(fun:str, *ints):
	if fun == 'add':
		return reduce(lambda x,y: x+y, ints)
	if fun == 'mul':
		return reduce(lambda x,y: x*y, ints)

 
# **kwargs
'''
The **kwargs allows function to receive an arbitrary number of keyword-value pair arguments.
Keyword-value arguments require argument name and value to be specified in function calls. 
These arguments are stored in a dictionary structure and can be the used inside the function to perform the desired task.
'''
def printkv(**args):
    for key,value in args.items():
        print("{}.{}".format(key,value))


# %%
# Functions as First Class Objects
'''
Functions in Python are objects. They can be passed and stored in variables, just like you do with objects
Since functions are objects, they can be even passed as arguments to other functions.
'''

muladd = addmul

muladd('add', 1,2,3,4)


def hello_eng(name:str):
    return "Hello {}!".format(name)

def hello_jap(name:str):
    return "こんにちは {}!".format(name)

def greet(lang, name:str):
    print(lang(name))

greet(hello_jap, "Fahad")


# %%
# Functions inside Functions
'''
Functions inherit the scope of the parent, so a function defined directly in a .py script file can be used anywhere
 inside that file. Similarly, functions defined inside classes or an existing code block maintain their existence 
 inside that definition scope.

Since both variables hold function references, the variables now behave as functions themselves and can be called!

When a function is first called, Python creates a small environment for that function that holds all the instructions 
and variables required for the function to execute. That environment inherits from the main Python environment so that 
default Python functions, operations or any custom library imports can be used inside that environment. Normally after a 
function is executed, that environment is destroyed to free up memory. In our case, we are actually returning a reference 
to a function inside that small environment. Since that reference is now bound to a variable (such as ctr_1), Python 
doesn’t automatically deletes that environment in its garbage collection routine. This allows the variables inside that 
function, such as curr, to remain in memory, allowing us to perform a simple increment operation by simply calling the 
function again
'''

def counter(start:int = 0):
    def _fun():
        nonlocal curr
        curr += 1
        return curr
    curr = start
    return _fun


ctr_1 = counter()
ctr_2 = counter()

# repeat commannds in prompt
ctr_2()
ctr_1()

# %%

# Function Decorators

from timeit import default_timer as timer
from functools import reduce

def Timer(arg):
    def decorator(func):
        def fun(*args):
            start = timer()
            out = func(*args)
            stop = timer()
            elapsed = stop-start
            if units == 'ms':
                elapsed *= 1000
            print('Elapsed Time: {}'.format(elapsed))
            return out
        return fun
    if callable(arg):
        # Expecting default argument since arg is a function
        # Set default to seconds
        units = 's'
        return decorator(arg)
    else:
        # Expecting argument here
        if arg in ['s', 'ms']:
            units = arg
            return decorator
        else:
            # Throw an exception here
            return None


@Timer
def add(*args):
    return reduce(lambda x,y: x+y, args)


print(add(1,2,3,4))

# %%
# reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
#  mentioned in the sequence passed along.

import functools

lis = [1, 3, 5, 6, 2, 30]
# sum of list
print(functools.reduce(lambda a, b: a+b, lis))
# max element in list
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# accomulate()
'''
reduce() stores the intermediate result and only returns the final summation value. 
Whereas, accumulate() returns a iterator containing the intermediate results. 
The last number of the iterator returned is summation value of the list.
'''

# importing itertools for accumulate()
import itertools
 
# importing functools for reduce()
import functools
 
# initializing list
lis = [1, 3, 4, 10, 4]
 
# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x+y)))
 
# printing summation using reduce()
print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x+y, lis))

# %%
