#%%
from importlib.resources import path
from inspect import stack
from tkinter.messagebox import NO
from typing import Iterable, List
import inter3

# read tokens to db in dictionary form
def append_to_db4 (db_dict_tokens, token) -> dict:
    if token == '':
        db_dict_tokens['_end'] = '_end'
        return db_dict_tokens
    
    first_char = token[0]

    if first_char not in db_dict_tokens:
        db_dict_tokens[first_char] = {}
        if len(token) == 1:
            rest = ''
    rest = token[1:]
    append_to_db4(db_dict_tokens[first_char], rest)
    
    return db_dict_tokens

def load_tokens4(fpath):
    tokens = inter3.load_tokens3(fpath)
    db_dict_tokens = {}
    for token in tokens:
        append_to_db4(db_dict_tokens, token)
    return db_dict_tokens

# returns a list of tokens from my_db
def flatten_dict(my_db : dict) -> list:
    from pandas.io.json._normalize import nested_to_record    
    res = []

    flat = nested_to_record(my_db, sep='')
    for key in flat:
        if key.endswith('_end'):
            
            tmp = key[0:-4]
            res.append(tmp)
    return res

def measure_time(func):
    import timeit
    def inner (*args, **kwargs):    
        print("time elpased for get_completions4 " + str(timeit.timeit(func(*args, **kwargs))))

    return inner

'''
def iter_suffixes(my_db):
    yield ''



# agrregator 
def collect_suffixes(my_db, limit):
    res = []
    for suffix in iter_suffixes(my_db=my_db):
        if len(res) == limit:
            break
        res.append(suffix)
    return res
'''

# @measure_time
# TODO. seperate function to 2 fuctions: get subtree after prefix. 
# collect all suffix with yeild - 
# create method iter_suffixes(my_db) which can be used in next form (yeild) 
# create func add_to_db
def get_completions4(my_db: dict, prefix: str, limit: int = 20) -> list:
    flat_dict = flatten_dict(my_db)
    
    res = []
    i = 0
    ctr = 0
    while ctr < limit and i < len(flat_dict):
        if flat_dict[i].startswith(prefix):
            res.append(flat_dict[i])
            ctr += 1
        i += 1
    return res

################################
def find_prefix(mdb:dict, prefix: str) -> dict:
    if prefix == '':
        return mdb
    else:
        first = prefix[0]
        if first in mdb:
            return find_prefix(mdb[first], prefix[1:])


def get_single_suffix(sub_dict:dict, res:str='', pathlist:List=[]):
    for k in sub_dict:
        
        if k != '_end':
            res += k 
            pathlist.append(k)
            next(get_single_suffix(sub_dict[k], res, pathlist))     
        elif sub_dict[k] == {}:
            sub_dict.pop(k)
        elif k == '_end':
            sub_dict.pop(k)
            yield res    

'''
def get_single_suffix_2(sub_dict:dict, res:str='', pathlist:List=[]):        
    stack = []
    curr_node = sub_dict

    while True:
        if curr_node is not '_end':
            curr_node = curr_node[0]

        else:
            break
'''

def iterate_suffixes2(mdb:dict) -> Iterable[str]:
    
    curr = mdb
    res = ''
    while True:
        for k in curr.keys():
            sub_node = curr[k]
            if k == '_end':
                res.join(k)
                yield res
            else:
                curr = curr[k]
                continue
    



def iterate_suffixes(mdb:dict):
    root_db = {'root' : mdb}
    yield get_single_suffix(root_db['root'])
    
  

def get_completions(my_db: dict, prefix: str, limit: int = 20) -> list:
    completions = []
    if my_db == {}:
        return completions
    suffix_dict = find_prefix(my_db, prefix)
     
    i=0
    while i<limit:
        single_suffix = iterate_suffixes2(suffix_dict)
        completions.append(next(single_suffix))
        i+=1
    return completions

# recursive method that find the prefix in the trie-dict and return a dict that contain the suffixes for a specific prefix 

def retrive_suffixes_by_prefix(mdb, prefix, limit) -> List[str]:
    pass



# %%
# test 1
my_db = {}
my_db = load_tokens4("tokens.txt")

print('my_db =')
print(my_db)


# get_completions_fedor(my_db, 'ba')
completions_list = get_completions(my_db, 'ba')
print(completions_list)

# %%
db_suffix = find_prefix(my_db, 'ba')
print(db_suffix)


#%%

prefix = 'ba'
print('tokens that have prefix \'' + prefix + '\':')
print(get_completions4(my_db, prefix, limit=1))

#%%

prefix = 'ra'
print('tokens that have prefix \'' + prefix + '\':')
print(get_completions4(my_db, prefix))

#%%

prefix = 'mar'
print('tokens that have prefix \'' + prefix + '\':')
print(get_completions4(my_db, prefix))

# %% different tokens
my_db = {}
my_db = load_tokens4("tokens2.txt")
print(my_db)

# %%
prefix = 'bal'
print('tokens that have prefix \'' + prefix + '\':')
print(get_completions4(my_db, prefix))

# %%
strtest = 'a'
strtest[2:]
# %%
