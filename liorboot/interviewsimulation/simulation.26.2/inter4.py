#%%
import inter3

# read tokens to db in dictionary form
def append_to_db4 (db_dict_tokens, token) -> dict:
    if token == '':
        db_dict_tokens[None] = None
        return db_dict_tokens
    
    first_char = token[0]

    if first_char not in db_dict_tokens:
        db_dict_tokens[first_char] = {}
        if len(token) == 1:
            rest = ''
        else:
            rest = token[1:]
        append_to_db4(db_dict_tokens[first_char], rest)
    return db_dict_tokens

def load_tokens4(fpath):
    tokens = inter3.load_tokens3(fpath)
    db_dict_tokens = {}
    for token in tokens:
        append_to_db4(db_dict_tokens, token)
    return db_dict_tokens

def nested_dict_search4(my_db : dict, prefix : str):
    if prefix == None:
        return ''
    else:
        if prefix[0] in my_db[prefix]:
            return  prefix[0] + nested_dict_search4(my_db[prefix], prefix[1:])
            

def get_completions4(my_db : dict, prefix : str) -> list:
    res = []
    ctr = 0
    while ctr < 20:
        word = nested_dict_search4(my_db, prefix)
        res.append(word)
        ctr += 1

    return res


my_db = load_tokens4("tokens.txt")
print(my_db)
# %%


# %%
print(get_completions4(my_db, "baron"))
# %%
