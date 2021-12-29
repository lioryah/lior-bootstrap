# Python tutorials summary
Tutorial 1 - https://www.mygreatlearning.com/blog/python-tutorial-for-beginners-a-complete-guide/

Tutorial 2 - https://www.youtube.com/watch?v=_uQrJ0TkZlc&ab_channel=ProgrammingwithMosh



- [Python tutorials summary](#python-tutorials-summary)
- [Comment](#comment)
- [Variables](#variables)
- [Operators](#operators)
  - [Arithmetic operators](#arithmetic-operators)
  - [Boolean Arothmatic](#boolean-arothmatic)
  - [Arithmetic operations order](#arithmetic-operations-order)
- [## Assignment operators](#-assignment-operators)
- [## Comparison operators](#-comparison-operators)
  - [Logical operators](#logical-operators)
  - [Identity operators](#identity-operators)
  - [Membership operators](#membership-operators)
  - [Bitwise operators](#bitwise-operators)
  - [Ternary Operator](#ternary-operator)
- [Lambda function](#lambda-function)
- [Arrays](#arrays)
- [Classes](#classes)
- [Inheritance](#inheritance)
- [Difference between methods and functions](#difference-between-methods-and-functions)
- [Iterators](#iterators)
- [Scope](#scope)
- [Modules](#modules)
- [Dates](#dates)
- [Random Number Generator in Python](#random-number-generator-in-python)
- [GENERATING VALUES FROM A GIVEN SEQUENCE:-](#generating-values-from-a-given-sequence-)
- [JSON](#json)
- [Regular expression](#regular-expression)
- [PIP](#pip)
- [Try, Except](#try-except)
- [User Input](#user-input)
- [Strings](#strings)
- [String Formatting](#string-formatting)
- [Python Data Types](#python-data-types)
- [Type conversion](#type-conversion)
- [Flow control statements](#flow-control-statements)
  - [Conditional statements (if-else statements)](#conditional-statements-if-else-statements)
  - [Looping (while and for statements)](#looping-while-and-for-statements)
    - [Nested for loop](#nested-for-loop)
- [File handling](#file-handling)
- [Creating Functions in Python](#creating-functions-in-python)
- [Learn Simple Commands by Using Python as a Calculator](#learn-simple-commands-by-using-python-as-a-calculator)
- [Data Manipulation with Pandas](#data-manipulation-with-pandas)

# Comment 
'#' symbol. Only 1 line 
For multiple lines use ``` ........ ```


# Variables

* Variable name begins with letter or underscore character
* Alpha-numeric and underscores are allowed in the rest of name
* Variable names are case-sensitive

```python
# different values assigned to many variables  
length, width, depth = 5, 8, 7  
# same value assigned to many variables  
length = width = depth = 5 
```

# Operators

## Arithmetic operators
```python
a = 2 
b = 5
print (a ** b)   # exponentiation  
print (a // b)    # floor division  
```
## Boolean Arothmatic
* or
* and
* not
* == (equivalent)
* != (not equivalent)

## Arithmetic operations order
Parenthesis
Exponentiation
Multiplication or division
Addition or subtraction

## Assignment operators
=
## Comparison operators
==
## Logical operators
Condition1 and condition2  # need to have both condition true to return true
Condition1 or condition2  # need to have only 1 condition true to return true
Not condition1  # return change of boolean 

## Identity operators
```python
a = ["hello", "world"]  
b = ["hello", "world"]  
c = a  
# prints true as both are same element  
print(a is c)  
# prints false as they are two diffent values  
# content may be same, but value locations are different  
print(a is b)   
# comparing the values gives true  
print(a == b)  
# not negates the comparison result  
# if two variables are not same, then result is true  
print(a is not c)  
print(a is not b)  
```

## Membership operators
Checks if an element is present in a given list.

```python
a = ["hello", "world"]   
# checks if given element is present in the a list  
print("world" in a)   
# checks if given element is not present in the a list  print("world" not in a)
```

## Bitwise operators
```python
a = 1   # binary equivalent of 1 is  1  
b = 2   # binary equivalent of 2 is 10  
  
# In case of AND(&) operation, if both bits are 1, set result to one 
# OR operation (|), gives 1 if either operands are 1 
# XOR (^) returns 1 if only one of the operands is 1 
# NOT (~) operation negates the bit value 
# zero fill left shift (<<) 
# signed right shift (>>) 
```

## Ternary Operator
an operator that works with three operands (components) 
The three components are (1) A condition (2) True value (3) False value.

```python
Age = 21
"Major" if (Age > 18) else "Minor"

Age = 21
"Major" if (Age > 18) else "Minor"
def is_major(Age):
       return 'Major' if Age > 18 else 'Minor'
# ShortHand Ternary operator

```

# Lambda function

Lambdas are anonymous, small functions.  The body of the lambda can have only one expression. Lambda can take any number of arguments.

```python
x = lambda a : a + 10
print(x(5))
```
The power of lambda is better shown when you use them as an anonymous function inside another function.

```python
def myfunc(n):
  return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11)) # 22
print(mytripler(11)) # 33

```
# Arrays
Square brackets are used to define a list.
They start from zero.

* len()
* append() method adds a new element to the end of the array.
* pop() method takes the array index and removes the element in the particular position
* remove() accepts the value of the element and removes it.

# Classes
Objects are entities that possess properties and methods.  These objects can be created by declaring classes. Classes are blueprints of objects.

```python
# create a class with "class" keyword  
class Fruit:  
    # a property, "name" is created  
    # the property is assigned with the value "mango"  
    name="mango"  
# let us create an object, "oneFruit" using the above class  
oneFruit = Fruit() 
```

All classes have an inbuilt function, __init__()
This function is called automatically when a new object is created from the class.

```python
# create a class with "class" keyword  
class Fruit:  
    # define the init function  
    def __init__(self, name, color):  
        self.name = name  
        self.color = color  
  
# let us create an object, "oneFruit" using the above class  
# values are passed to the class  
oneFruit = Fruit("mango", "yellow")  
  
# the property of the object "oneFruit" is accessed like this  
print(oneFruit.name)  
print(oneFruit.color)  

# makeJuice() method inside the class
def makeJuice(self):  
        print("Made " + self.name + " juice. It will be in " +   
            self.color + " color.") 

# The property of the object can be modified like this:
oneFruit.color = "red" 
```

# Inheritance
Inheritance is a concept where we extend the functionality of a class to create new classes.

```python
class Vehicle:  
    def __init__(self, make, color):  
        self.make = make  
        self.color = color  
  
    def display(self):  
        print("make= " + self.make + " color= " + self.color)  
  
# v = Vehicle("2015", "green")  
# v.display()  
  
class Car(Vehicle):  
    def __init__(self, make, color, numOfSeats):  
        super().__init__(make, color)  
        self.numOfSeats = numOfSeats  
  
    def display(self):  
        super().display()  
        print("number of seats= " + str(self.numOfSeats))  
  
    def wipeWindshield(self):  
        print("turned on wiper")  
  
newCar = Car("2019", "orange", 5)  
newCar.display()  
newCar.wipeWindshield()  
```

# Difference between methods and functions
Functions are general purpose and not relates to any kind of object (print(), len())
Methods usually relate to a specific object such as upper() for a string object. To access a method we use . i.e. str.upper()

# Iterators
Iterator is a container of values, with which we can traverse through all the values.

Lists, tuples, dictionaries, and sets are iterable and implement an iterator protocol.

```python
fruitTuple = ("mango", "apple", "grapes")    
fruitIter = iter(fruitTuple)  
print(next(fruitIter))  

# A string can be iterated using iter() method.
fruitStr = "mango"  
fruitIter = iter(fruitStr)  
print(next(fruitIter))  

# The iterable object can be iterated with the for in loop.
for fruit in fruitTuple:  
    print(fruit)  
```

We can create our own iterator class.  We need to implement __iter__() and __next__() methods.

```python
class Fibonacci:  
    def __iter__(self):  
        # define first two numbers  
        self.first = 1  
        self.second = 2  
        return self  
  
    def __next__(self):  
        curr = self.first + self.second # find new number  
        if (curr <= 50):  
            self.first = self.second # shift the previous two numbers  
            self.second = curr  
            return curr  
        else:  
            raise StopIteration  
  
fibo = Fibonacci ()  
fiboIter = iter(fibo)  
  
for f in fiboIter:  
    print(f)  
```
if the Fibonacci series has reached 50.  Any value beyond or equal to 50 would raise an error. That would stop the for loop.

# Scope
The variable is available only in the region that it is declared.  The limitation of such variable declaration is scope.

Variable created at the main level are global and can be accessed inside the function definition.

When the same name is used for variables inside and outside a function, then python treats them as two separate variables.
If we change the value of a inside the function, that change won’t affect the variable outside the function.

While a variable is defined inside a function, the variable can be declared as global using the “global” keyword.

```python
def func1():  
    global a  
    a = 10  
```

# Modules
Module is about using library files.  You create a python library file with general functions and variable declarations. These definitions can be referred to by another python file.

```python
# inventory.py
fruits = ["mango", "apple", "grapes"]    
    def countStock():  
    return len(fruits) 
 
# main.py
import inventory    
print(inventory.countStock())  
print(inventory.fruits) 
```

alias - change the library name to inv. change is local to our code.
```python
import inventory as inv  
```

The from clause is used to import part of the module.
```python
from  inventory import  countStock
```

# Dates
```python
import datetime  
# current date and timestamp
today = datetime.datetime.now()  
```

create a date object with a specific date value. hours, minutes, seconds, milliseconds are optional.  Zero is their default value.
```python
pastDate = datetime.datetime(2020, 2, 29) 
# %B returns a full month’s name.
print(pastDate.strftime("%B"))  
```

# Random Number Generator in Python
RANDINT()
```python
random.randint(a,b)  # a <= x <= b   (includes a and b)
```

RANDARANGE()
```python
random.randarange(a,b,c)
```
generates a number (given in range a-b) as specified and gives only numbers in steps multiples of c from a.
 
RANDOM()
```python
random.random()
```
produces floating-point values between 0.0 to 1.0 

UNIFORM()
```python
random.uniform(a, b)
```
generates decimal numbers in range (a, b)

# GENERATING VALUES FROM A GIVEN SEQUENCE:-
1. CHOICE()
random.choice([1,2,3,4,5,6,7,8,9])
returns random values from a sequence
2. SAMPLE()
random.sample([2, 3, 4, 5, 6, 7, 8], 3)
returns 3 random values from a sequence
3. SEED()
X = 2
Random.seed(x)
the output of the code remains the same for each time
4. SHUFFLE()
random.shuffle([1, 2, 3, 4, 5, 6, 7, 8])
changing the positions of the elements.

# JSON
Javascript object notation
It is a text format useful to exchange data and store information.

The json string can be parsed into json data using json.loads() method.  Json.loads 
method returns the json data a dictionary.
```python
import json  
  
jsonStr = '{ "name" : "mango", "price" : 100, "color" : "yellow" }'  
 
jsonData = json.loads(jsonStr)  
print(jsonData["color"]) 
```

json.dumps() is used to convert python objects into json strings.
```python

fruitsDictionary = { "name" : "mango", "price" : 100, "color" : "yellow" }   

jsonStr = json.dumps(fruitsDictionary) 
```

sort the order of the keys in the dumps method (alphabetically)
```python
jsonStr = json.dumps(fruitsDictionary, indent=5, sort_keys=True)  
```

# Regular expression
 a powerful search mechanism, where we have a string pattern and look for matching substring in a given full string.
```python
import re  
  
givenStr = "Hello world, good morning"  
outRegex = re.search("^Hello", givenStr)  
print(outRegex) 
```

# PIP
PIP is a package manager that helps in installing required modules.
```python
pip install <package-name>
pip uninstall <package-name>
pip list  # display all packages installed in this machine
```

# Try, Except
By using try, except, we handle the errors in our code and avoid code termination

finally is a block that gets executed after try and except are executed.  This gets the control irrespective of if error occurred or not. (cleaning operations like closing file)

```python
try:  
    print(a)  
except:  
    print("error occurred, please check if a is defined")  
finally:  
    print("We are here after try and except") 
```

We can write code to raise custom errors.  The error thrown can be handled by our try, except or the python engine can receive the error.
```python
a = 0  
  
if a == 0:  
    raise Exception("cannot divide by zero")  
```

# User Input
```python
city = input("Where do you live? ")  
print("city you live is : " + city) 
```

# Strings
* String can be declared by “...” or ‘...’
To use “ or ‘ in a string use ‘ or “ to declare a string respectively.
* Multi line string: start and ends with ‘’’
‘’’
…
…
‘’’
* Methods on strings: (all case sensitive)
    * str.upper()  # converts to all upper case letters
    * str.lower()  # converts to all lower case letters
    * str.find(str2)  # finds index of first instance of a str2 
    * str.replace(str2, str3)  # finds and replace all instances of str2 to str3
    * str.title() #  convert str to titlecase (every word is capitalized)
    * str2 in str # return boolean value if str contains str2 

# String Formatting
string variables can be formatted with format() method.  The template string is created first and values are attached at the formatting stage.
```python
tStr = "The fruit {} is {} color."  
print(tStr.format("mango", "yellow")) 
```

You may refer to the values using index or names.  The index is zero based.
```python
tStr = "The fruit {0} is {1} color. {0} is good for health"  
print(tStr.format("mango", "yellow")) 

tStr = "The fruit {name} is {color} color. {name} is good"  
print(tStr.format(name = "mango", color = "yellow")) 
```
# Python Data Types
1. Numbers
    * int (signed integers)
    * long (long integers, they can also be represented in octal and hexadecimal)
    * float (floating point real values)
    * complex (complex numbers with imaginary number represented with ‘j’)


2. String
A single, double or triple quotes can be used to define a string in Python.

    * “hello” +” python” will return “hello python”
    * “Python ” *2 will return “Python Python “
    * Str1[0:2]     printing first two character using slice operator    
    * Str1[4]     printing 4th character of the string  

3. List
A list can contain data of different types, it is similar to arrays in C.

To access data from a list, slice [:] operators should be used. Repetition operator (*) and concatenation operator (+) work the same way in strings as well as list.


```python
 l  = [1, "hi", "python", 2]
```

4. Tuple
Tuple contains the collection of items of different data types, these items are separated with a comma (,) and need to be enclosed within parentheses ().
The size and value of items in a tuple cannot be modified since it is a read-only data structure.


5. Dictionary
A dictionary is like an associative array where each key stores a specific value. It is an ordered set of key-value pair items. A key is capable of holding any primitive data type. Value is an arbitrary Python object. Each item in a dictionary is separated using a comma and is enclosed within curly brackets {}

```python
d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}
```
# Type conversion
* int() 
* float()
* bool()

type(var) - return type of var

# Flow control statements

## Conditional statements (if-else statements)
```python
if (a>b) & (a>c):
    print (“a is the greatest”)
elif (b>a) & (b>c):
    print (“b is the greatest”)
else: 
    print (“c is the greatest”)
```

## Looping (while and for statements)
* While
```python
l1=[...]
i=0
while i<len(l1):
    ...
    i=i+1
```

* for
```python
l1 = [“blue”,“green”,”red”]
for i in l1
    print(i)
```

The iterations start with i=0. The for loop has an iterator that increases itself each run.

### Nested for loop
```python
color = [“green”,“yellow”,“pink”]
item = [“chair”,“book”,“phone”]
for i in color:
    for j in item:
        print(i,j)
```

# File handling
open ()  
takes two parameters, one is the file name we want to operate and other is a mode
Mode:  read (r) or append (a) or write (w) or create (x). we can specify if the file is binary (b) or text (t) file

Creating a file place this file in the same directory as the python code we are writing

When using one parameter default mode is assumed. text file is opened in read mode.
```python
f = open("fruits.txt")

# Its equal to
f = open("fruits.txt", "rt") 
```

The open returns a file object.  This file object is used to read or write into the file.
```python
print(f.read())
```
read method of file object loads the content of the text file and returns as a string
```python
print(f.readline())

```
readline() method returns one line of text.

```python

```
All the lines can be read within a for loop.
```python
for line in f:  
    print(line) 
```

When the file usage is over, it is better to close the file
```python
f.close()
```
Writing into a file
append (a) mode will add new strings to the end of the file. 
write (w) mode will remove existing content of the file and write the new string alone into the file.
```python
f = open("fruits.txt", "a")  
f.write("guava is green")  
f.close() v
```

If we replace mode “a” with “w”, the whole text file (existing content) will be erased and only the new string will be available in the file.

mode x is used to create a new file.  If the file already exists, x will throw an error saying file already exists.

mode x and w will create new file if the file does not exist.

The os library is used to delete folders and check if files exist. Error is thrown if the file doesn’t exist.

```python
import os  
  
os.remove("fruits.txt")  
 
```
check if the file exists or not 
```python
if os.path.exists(filename):  
    os.remove()  
```
A folder can be deleted with rmdir() method of os module.
```python
import os  
  
os.rmdir("unwantedFolder")  
```


# Creating Functions in Python
To create functions in Python, we will use the ‘def’ method. Any input parameter or arguments need to be placed inside the parenthesis with the functions name while defining it. The code block within every function starts with a colon (:) and is indented. Finally, return [expression] exits a function. Look at the example below.
```python
 def add_10(x):
     return (10+x)
```


# Learn Simple Commands by Using Python as a Calculator
the last printed value, assigned to _
```python
 >>> price = 110.5013.8125   # this is the last printed value, hence assigned to _
```
```python
 >>> price + _
```
# Data Manipulation with Pandas
Pandas stands for Panel Data. It is the core library for data manipulation and data analysis. 
NumPy provides us with a multidimensional array, similarly, Pandas provides us with a multi-dimensional data structure to perform various data manipulation operations. 

The single-dimensional data structure is called a series object; the multidimensional data structure is known as data-frame.

In Pandas, the series object is a one-dimensional labelled array. When we consider NumPy array, it is not labelled. 
```python
 import pandas as pd
s1= pd.Series ([1,2,3,4,5]) 
```

A data-frame is a two dimensional labelled data structure and it comprises rows and columns. Normally, in a data-frame, all the elements in a particular column are of the same type. 

```python
 pd.DataFrame(student) 
```
The key becomes the column name and the list of values for a particular key becomes the row values for that column. In simpler words, the key here is student_name and the row values are Bob, Sam, Julia and Charles. 

There are a few inbuilt functions which can be performed on any data frame. They are – head(), shape(), tail() and describe(). If we want to separate individual rows and columns from a data frame, we can use any of these two methods. They are .iloc[] and .loc[] method. 


