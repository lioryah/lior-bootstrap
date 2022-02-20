'''
[1] => [[1]]
[1,2] => [[1,2], [2,1]]
[1,2,3] => [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
'''
#%%
import itertools
from sre_constants import BRANCH


def insert_in_list(element ,list_inp):
    res = []
    for i in range(len(list_inp)):
        new_perm = list_inp[0:i] + [element] + list_inp[i:]
        res.append(new_perm)
    res.append(list_inp + [element])
    return res

insert_in_list(4,[1,2,3])

assert insert_in_list(1,[]) == [[1]]


def permutate(list_inp):
    all_perm = []
    
    if len(list_inp) == 0:
            return list_inp
    
    if len(list_inp) == 1:
            return [list_inp]
    
    head = list_inp[0]
    rest = list_inp[1:]

    small_perm = permutate(rest)
    for single_perm in small_perm:
        res = insert_in_list(head, single_perm)
        all_perm.extend(res)
    
    return all_perm

assert len(permutate([1,2,3,4])) == 4*3*2*1
#permutate([2])

 
#%%
def permutate_no_memory(list_inp):

    single_perm = []
    original_inp = list_inp.sort()
    
    for i in range(original_inp):  
        
        print 
        single_perm.append(original_inp[i])

        for j in reversed(range(original_inp)):
            j = 2
    for item in list_inp:
        single_perm.append(item)
        while(len(single_perm) < len(list_inp)):

            for next_item in list_inp[item:]:
                single_perm.append(next_item)

                if len(single_perm) == len(list_inp):
                    print(single_perm)
                    continue
    return 1


# %%
def permutations(s):

	# create a list to store (partial) permutations
	partial = []

	# initialize the list with the first character of the string
	partial.append(s[0])

	# do for every character of the specified string
	for i in range(1, len(s)):
		# consider previously constructed partial permutation one by one

		# iterate backward
		for j in reversed(range(len(partial))):

			# remove the current partial permutation from the list
			curr = partial.pop(j)
			# Insert the next character of the specified string into all
			# possible positions of current partial permutation.
			# Then insert each of these newly constructed strings into the list

			for k in range(len(curr) + 1):
				partial.append(curr[:k] + s[i] + curr[k:])

	print(partial, end='')

s = "1234"


permutations(s)
# %%
import itertools
s = [1, 2, 3, 4]

itertools.permutations(s, 4)


# %%
iterable = "ABCD"
pool = tuple(iterable)
n = len(pool)

indices = list(range(n))

tuple_of_ind = tuple(pool[i] for i in indices[:n])
print(pool)


# %%
def permutations_new(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                yield indices
                yield cycles
                break
        else:
            return


for x in permutations_new("ABC"):
    print(x)
    
    # %%
