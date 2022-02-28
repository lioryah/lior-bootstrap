#%%
'''
input: [ 5,5,5,3,3,1,1,7,7,7]
ouput: 3
'''

def count_changes(in_arr):
    ctr = 0
    for i in range(1,len(in_arr)):
        if in_arr[i] != in_arr[i-1]:
            ctr += 1
    return ctr

count_changes([])
