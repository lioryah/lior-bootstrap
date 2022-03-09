
def clean_token(token):
    if token.endswith('\n'):
        return token [:-1]
    return token


def iter_tokens_list(fpath):
    f_tokens = open(fpath, "r")
    db_tokens = []
    i = 0
    for line in f_tokens:
        token = clean_token(line)
        yield token
    return db_tokens


def append_to_db (db_dict_tokens, token) -> dict:
    if token == '':
        db_dict_tokens['_end'] = '_end'
        return db_dict_tokens
    
    first_char = token[0]

    if first_char not in db_dict_tokens:
        db_dict_tokens[first_char] = {}
        if len(token) == 1:
            rest = ''
    rest = token[1:]
    append_to_db(db_dict_tokens[first_char], rest)
    
    return db_dict_tokens

def load_tokens(fpath):
    db_dict_tokens = {}
    for token in iter_tokens_list(fpath):
        append_to_db(db_dict_tokens, token)
    return db_dict_tokens