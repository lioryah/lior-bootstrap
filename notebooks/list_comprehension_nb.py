
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
from numpy import size


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

multi_2 =  map(lambda x: x*2, new_list)
type(multi_2)


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


# %%
# create a list of numbers from 1 to 1000
list1000 = []
list1000 = [x+1 for x in range(1000)]
# print(list1000)

numbers = []
for i in range(1,1001):
   numbers.append(i)
numbers


# %%
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)


# %%
# set of questions from https://towardsdatascience.com/beginner-to-advanced-list-comprehension-practice-problems-a89604851313
nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

div_by_8 = [x for x in nums if x % 8 == 0]
div_by_8


# %%
contain_6 = [x for x in nums if "6" in str(x)]
contain_6


# %%
spaces_list = [x for x in string if " " in str(x)]
num_of_spaces = print(len(spaces_list))


# %%
string_parsed = string.split()
less_than_5_letters = [x for x in string_parsed if len(x) < 5]
print(less_than_5_letters)


# %%
string_parsed = string.split()
string_to_dict_comp = {key : len(key) for key in string_parsed}
print(string_to_dict_comp)


# %%
div_by_single_digit = [x for y in range(2,10) for x in range(1,1001) if x%y == 0]
print(sorted(div_by_single_digit))
# %%
div_by_high_single_digit = {x : y for x in range(1,1001) for y in range(2,10) if  x % y == 0}
print(div_by_high_single_digit)
# %%


# %%

# %%

# %%

# %%
