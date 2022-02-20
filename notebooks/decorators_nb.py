#%%
# Decorators


#%%
'''
A decorator is a function that takes another function as an argument, does some actions, and then returns the argument 
based on the actions performed.
a decorator is a callable that accepts and returns a callable.
    
    * callable() -  callable is something that can be called. 
    This built-in method in Python checks and returns True if the object passed appears to be callable, but may not be, otherwise False.
'''
# %%
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

ordinary() 

pretty = make_pretty(ordinary)
pretty()

# %%
'''
In the example shown above, make_pretty() is a decorator
The function ordinary() got decorated and the returned function was given the name pretty.# %%

'''

# %%
'''
Generally, we decorate a function and reassign it as:

ordinary = make_pretty(ordinary)

We can use the @ symbol, for example:

'''
# %%
@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

# %%
