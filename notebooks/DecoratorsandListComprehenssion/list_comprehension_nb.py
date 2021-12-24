
'''
used for creating a new list based on the values of an existing list.
syntax:
newlist = [expression for item in iterable if condition == True]

* condition is like a filter that only accepts the items that valuate to True. The condition is optional and can be omitted
* The iterable can be any iterable object, like a list, tuple, set etc.
* expression is the current item in the iteration, but it is also the outcome,
 which you can manipulate before it ends up like a list item in the new list. 
 The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome.
 
 '''

#%%

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# equivelant to:

newlist = [x for x in fruits if "a" in x]
print(newlist)

def to_x(x):
  _it = x if x != "banana" else "orange"
  return _it



newlist = [to_x(x) for x in fruits] # banana should change to orange
print(newlist)

# %%
new_list = [x for x in range(1,1001)]
new_list

# %% 
new_multi = [x*2 for x in new_list]
new_multi

# %% 

multi_2 = list(map(lambda x: x*2, new_list))
multi_2

# %%
 
# no_fours = (x for x in multi_2 if x%4 == 0)
# no_fours
# %%
def gen_fours(_list):
    _no_fours = (x for x in _list if x%4 == 0)
    for y in _no_fours:
        yield y


# no_fours = gen_fours(multi_2)       
# no_fours
# %%
second_pow = [x*x for x in gen_fours(multi_2) ]
second_pow
# %%
if x == 4:
    y = 5
else:
    y = 10


# %%
w  = 5 if x == 4 else 10