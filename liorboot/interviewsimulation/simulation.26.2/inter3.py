#%%
# search completion system (i.e. google search string)

# read tokens to db
# parameter - path to tokens file
# return an object that represent the db
def load_tokens3(fpath):
    f_tokens = open(fpath, "r")
    db_tokens = []
    i = 0
    for line in f_tokens:
        db_tokens.append(clean_token3(line))
    return db_tokens


def clean_token3(token):
    if token.endswith('\n'):
        return token [:-1]
    return token

# return all tokens(words that starts with provided prefix
def get_completions3(my_db, prefix):
    res = []
    for entry in my_db:
        if entry.startswith(prefix) :
            res.append(entry)
    return res


#%%
my_db = load_tokens3("tokens2.txt")
my_db
# %%

print(get_completions3(my_db, "bal"))
