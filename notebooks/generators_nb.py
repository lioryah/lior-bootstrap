# %%
# creating a generator object. usable only once
def gen_seq():
    yield 5
    yield 6
    yield 7
    
gen_seq()
# %%

# %%
# create a generator 
gen_single = (x  for x in (1, 2, 3))
gen_single
# %%

[x  for x in (1, 2, 3)]
# %%
# creating a list with x:x 
{x : x  for x in (1, 2, 3) }

# %%
# create a list by using a generator 
{x : x  for x in gen_seq() }

# %%
# example how the_seq which is a reference to a generator is used only once. 
the_seq = gen_seq()
the_seq

for x in the_seq:
    print(x)
    break

for x in the_seq:
    print(x)
    break

for x in the_seq:
    print(x)
    break

for x in the_seq:
    print(x)
    break

for x in the_seq:
    print(x)
    break



# %%

# since gen_seq is creating a new generator we can still use it
seq=gen_seq()
{x : x  for x in seq }  # why doesnt it print the first list??
{x : x  for x in seq }

# %%
