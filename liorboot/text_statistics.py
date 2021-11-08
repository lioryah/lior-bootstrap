import os

path1 = '/mnt/c/users/liory/_wd/repos/lior-bootstrap/txt/txt1.txt'
path2 = '/mnt/c/users/liory/_wd/repos/lior-bootstrap/txt/txt2.txt'

path_list = [path1, path2]


# part 1
# print tokens statistics for txt file with path as arg
def stat_per_file(path):
    print(f"Stats for file in path: {path}")
    f = open(path, 'r')
    text = f.read()
    f.close()

    tokens_arr = text.split()
    token_dict = {}

    for token in tokens_arr:
        if token in token_dict:
            token_dict.update({token : token_dict[token] + 1})
        else:
            token_dict.update({token : 1})
    
    return token_dict

    
def print_dict(token_dict):
    for x,y in token_dict.items():
        print(x, ': ', y)


# part2
# print tokens statistics for directory or list of txt files paths
def stat_per_batch(path_list):
    path_list2 = []
    
    if type(path_list) == dir:
        for f in dir:
            filepath = os.path.join(os.path.dirname(f), 'txt.txt')
            path_list2.append(filepath)
    else:
        path_list2 = path_list

    total_list_stat = {}
    for path in path_list2:
        curr_stat = stat_per_file(path)
        for key in curr_stat:
            if key in total_list_stat:
                total_list_stat.update({key: total_list_stat[key] + curr_stat[key] })

            else:
                total_list_stat.update({key: curr_stat[key]})
            
    return total_list_stat


# part 3
# print in how many files token X appears
def token_appearences_files(path_list, token):
    token_appearences = 0
    for path in path_list:
        curr_stat = stat_per_file(path)
        for key in curr_stat:
            if key == token:
                token_appearences += 1
            
    return token_appearences

'''

total (in all the text)
token in files statistics
for term X show in how many files appears X

python textcount.py text-file1.txt text-file2.txt

programm can receive one path to directory instead of list of paths, list all files in this dir and perform same action.


'''




def main_():
    # dict = stat_per_file(path1)
    # print_dict(dict)

    #print_dict(stat_per_batch(path_list))
    token = 'went'
    i = token_appearences_files(path_list, token)
    print(f'token appearances of {token} is {i}')
    
if __name__ == '__main__':
    main_()
