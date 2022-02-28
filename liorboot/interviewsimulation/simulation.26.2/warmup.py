#%%
'''
input: 2 3 5 2 3 3
output: {2 : 2, 3: 3, 5: 1} 
'''

def count(in_arr):
    res = {}
    for x in in_arr:
        if x not in res:
            res[x] = 0
        res[x] +=1
    return res

count([2, 3, 5, 2, 3, 3])

# %%
