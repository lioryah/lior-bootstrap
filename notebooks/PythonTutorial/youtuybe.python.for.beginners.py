# Python Tutorial - Python for Beginners [Full Course]

# link to reference: https://www.youtube.com/watch?v=_uQrJ0TkZlc&ab_channel=ProgrammingwithMosh

# %%
# car game
import io
from os import NGROUPS_MAX
from typing import MutableMapping
def car_game ():
    help_prompt = '''
    start - to start the car
    stop - to stop the car 
    quit - to exit
    '''
    while True:
        user_input = input("")
    
        if user_input == "start":
            print("car started  - ready to go")
            continue
        elif user_input == "stop":
            print("car stopped")
            continue
        elif user_input == "quit":
            return exit(0)
        elif user_input == "help":
            print(help_prompt)
            continue
        else:
            print("i dont understand")
            continue

car_game()
# %%
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print("X" * number) 


# %%
# remove duplicates from a list excersize
num_list = [1, 3, 9, 2, 84, 9, 3]

def remove_duplicates_from_list(num_list):
    item_count = 0 
    
    for item in num_list:
        item_count = num_list.count(item)
        if num_list.count(item) > 1:
            num_list.remove(item)

remove_duplicates_from_list(num_list)
print(num_list)
# %%
# Unpacking - assign items in Tuples or Lists to smae number of variables
coordinates = (1, 2, 3)
x, y, z = coordinates
print(coordinates)

# %%
# Emoji converter excersize

user_inp = input(">")
words_list = user_inp.split(" ")

emojis = {
    ":(": "SAD",
    ":)": "SMILE"
}
output = ""

for word in words_list:
    new_word = emojis.get(word, word)
    output = output + new_word + " "
print(output)


# %%
from pathlib import Path

# absolute apth - a path starting from the root of the hadrdisk
# relative path - a path starting from the current directiry


path = Path()