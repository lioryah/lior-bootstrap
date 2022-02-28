#%%
def decorate(func):
    def inner (*args, **kwargs):
        x_in = kwargs['x']
        yu = x_in *x_in
        print("inner " + str(yu))

    return inner
    
@decorate
def foo(x):
    print("foo " + str(x))


# %%
foo(x = 3)

# %%
xs = [x for x in range(10)]
xy = [y for y in xs if y%2 == 0]

