# Learn Python - Full Course for Beginners [Tutorial]
# link to ref: https://www.youtube.com/watch?v=rfscVS0vtbw&ab_channel=freeCodeCamp.org

## variable and data types

#%%
from abc import ABCMeta


_str = "bootstrap for all"
print(_str.index("f"))  # return the first index of character

# %%
num = 5
print(str(num) + " is good") # converting number into a string

# %%
print(max("A","n"))

# %%

# recieve input from user
name = input("please enter name:")


# %%
# simple add numbers from user
num1  =input("enter a number:")
num2  =input("enter a second number:")
result = float(num1) + float(num2)
print("result is " + str(result))

# %%
# Lists
list1 = [5, 1, 2, 3]
list2 = ["ayelet", "lior"]
list3 = [5, 1, 2, 3]


list1.extend(list2)
print(list1)

list2.append(False)
print(list2)

list2.insert(False, 0)
print(list2)

list2.pop(False)
print(list2)

list2.reverse()
print(list2)

list3.sort()
print(list3)
# %%

# %%

# Tuples
# IMMUTABLE - u can not change them after creation

coordinate = (3,5)
print(coordinate)
# %%

# Functions
# a function can recieve parameters
def hi(name = input("whats your name")):
    print("hi " + str(name))

hi("moses")
hi()
# %%
# If 
if True and True:
    print ("and")
elif True or False:
    print("or")
# %%
# Dictionary. key,value pairs
# keys must be uniqe

month_conversion = {
    1 : "january",
    2 : "february",
    3 : "march"
}

print(month_conversion.get(2))
print(month_conversion.get(13, "not a valid month"))  # getting a default value for list

# %%

wood = ["pine", "cedar", "ipea"]

for woodtype in wood:
    print(woodtype + " is in index " + str(wood.index(woodtype)))
# %%
# 2D and nested 

number_grid = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [0]
 ]

print(number_grid[1][2])

for row in number_grid:
    print(row[0])
# %%
# converting all vowels into k's
def translate(phrase):
    result = ""

    for letter in phrase:
        if letter in "AEIOUaeiou":
            result = result +  "K"
        else:
            result = result + letter    
    return result

inp = input("enter a phrase:")
print(translate(inp))
# %%
# Try Except
try:
    value = 20/0
    number = int(input("enter a number:"))
    print(number)
except ValueError:
    print("invalid input")
except ZeroDivisionError as err:
    print(err)

# %%
# Read from file

employee_file = open("employees.txt", "r")  # r-read w-write a-append r+-rean and write
print(employee_file.readlines())

employee_file.close()

# %%
employee_file = open("employees.txt", "a")  # r-read w-write a-append r+-rean and write
employee_file.write("\nToby - HR")

print(employee_file)

employee_file.close()


# %%
emplyyees1 = open("emplyees1.txt", "w")
emplyyees1.write("all that time")
emplyyees1.close()
# %%

# Modules and PIP
# modules are any external python files that you wanna use stuff inside of it

# %%

# Classes and Objects

# with a class we can create our own data type
# a class defines the attributes an functionality of a data type. a template
# an object is an instance of that class

class Student:
    def __init__(self, name, major, gpa, is_a_senior):  # map out the attributes a student should have
        # next lines assign the parameters given to the actual instance (object) attribites
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_a_senior = is_a_senior
    
student1 = Student("lior", "buisness", 100, True)
student2 = Student("ayelet", "nursing", 100, True)
print(student1.name)
print(student2)

# %%
# multiple answers quiz
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer    

question_prompt = [

    "what is your name? \n(a)Lior \n(b)Feodor \n (c)Yair  \n\n",
    "what is your age?  \n(a)15 \n(b)34 \n (c)52 \n\n",
    "what is your favorite color? \n(a)green \n(b)blue \n (c)red \n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a"),

]

def run_test(questions):
    score = 0

    for question in questions:
        if input(question.prompt) == question.answer:
            score += 1
    print("your score is: " + str(score))

run_test(questions)
# %%

# Object functions

class Student:
    def __init__(self, name, major, gpa):  # map out the attributes a student should have
        # next lines assign the parameters given to the actual instance (object) attribites
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 90:
            return True
        else:
            return False



student1 = Student("lior", "buisness", 100)
student2 = Student("ayelet", "nursing", 80)            

print(student1.on_honor_roll())
print(student2.on_honor_roll())
# %%

# Inheritance
# 

class Phd_student(Student):
    def is_s_ta(self):
        print("Im a TA")

phd_student = Phd_student("moti", "law", 92)

print(phd_student.name)

phd_student.is_s_ta()

