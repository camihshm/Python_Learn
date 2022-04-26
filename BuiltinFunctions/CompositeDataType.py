#----------------------------------------------------------------------------------
## Built-in Functions: Composite Data Type.
#----------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# Function              | Description
#------------------------------------------------------------------------------------------------
# bytearray()           | Creates and returns an object of the bytearray class.
#------------------------------------------------------------------------------------------------
# bytes()               | Creates and return a bytes object (similar to bytearray but immutable).
#------------------------------------------------------------------------------------------------
# dict()                | Creates a dict object.
#------------------------------------------------------------------------------------------------
# frozenset()           | Creates a frozenset object.
#------------------------------------------------------------------------------------------------
# list()                | Creates a list object.
#------------------------------------------------------------------------------------------------
# object()              | Creates a new featureless object.
#------------------------------------------------------------------------------------------------
# set()                 | Creates a set object.
#------------------------------------------------------------------------------------------------
# tuple()               | Creates a tuple object.
#------------------------------------------------------------------------------------------------

# Example 1: Convert list() to bytearray().

from typing import Set


seq_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seq_numbers_converted = bytearray(seq_numbers)
print(seq_numbers_converted)

x = seq_numbers_converted[3]
print(x)
y = seq_numbers_converted[4:5]
print(y)
z = seq_numbers_converted[-8]
print(z)
w = seq_numbers_converted[2]
w = 4
print(w)

#------------------------------------------------------------------------------------------------

# Exampe 2: Convert bytearray() to bytes()
seq_numbers_converted = bytes(seq_numbers)
print(seq_numbers_converted)

x = seq_numbers_converted[1]
print(x)
y = seq_numbers_converted[1:7]
print(y)
z = seq_numbers_converted[-5]
print(z)
w = seq_numbers_converted[6]
w = 2
print(w)

# ATTENCION: The difference between bytesarray() and bytes() is bytes() is not mutable.
#------------------------------------------------------------------------------------------------

# Exampe 2: dict()
# Dictionary is a collection of key-value pairs, it's mutable data structure i.e so the data in 
# dict can be changed. You can be access the dictionary using indexes to return the specific
# value.

# Passing keywords arguments to dict() method
values = dict(a=1, b=2, c=3, d=4)
print(values)

# Passing key-values pairs mapped by colon to dict function
values = dict({'a': 1, 'b': 2, 'c': 3})
print(values)

# List of key values pairs is passed and keyword argument is also passed.
values = dict([('a', 1), ('b', 2), ('c', 3)], d=4)
print(values)  

#------------------------------------------------------------------------------------------------

# Example 3: frozenset()
# This functions is inbuilt function in Python which takes an iterable object as input and makes
# them immutable. Which means that elements from the frozenset cannot be added or removed once
# created.

# Tuple of numbers.
numbers = (1, 2, 3, 4, 5)

f_numbers = frozenset(numbers)
print("The object is :", f_numbers)

# Create a dictionary.
customers = {"name": "Ammit Salankar", "age": 33, "sex": "Male",
             "college": "MIT", "occupation": "engineer"}
key_value = frozenset(customers)
print ("The keys are:", key_value)

# Create a lits.
cars = ["BMW", "Mercedes", "Volvo", "Lexus"]
f_cars = frozenset(cars)

# If you try change the value in the list the application return an error.
# f_cars[2] = "Audi"

#------------------------------------------------------------------------------------------------

# Example 4: list()
# This function takes any iterable as a parameter and returns a list. In python iterable is the
# object you can iterate over.

# Create a list from a string.
alphabet = "ABCDEFGHIJKL"
alphabet_list = list(alphabet)
print(alphabet_list)

# Create a list from a tuple.
var = ('A', 'E', 'I', 'O', 'U')
var_list = list(var)
print(var_list)

# Create a list from set and dictionary.
set = {'A', 'B', 'C', 'D', 'E'}
set_list = list(set)
print(set_list)

dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
dict_list = list(dictionary)
print(dict_list)

#------------------------------------------------------------------------------------------------

# Example 5: object()
# An object is a instance of class and a class is like a blueprint while an instance is a copy of 
# the class with actual values. The objects are basically and encapsulation of data variables and
# methods acting on that data into a single entity.

# ATTENCION: The instance defining represent memory allocation necessary for storing the actual 
# data of variables.
# object = myClas() --this is a exemple of instance.

# Create object.
class Cars:
    def __init__(self, a, b):
        self.model = a
        self.price = b
BMW = Cars("X1", 120000)
print(BMW.model, BMW.price)

# Accessing class member usign object.
# Variables and methods of a class are accessible by using class objects or instances.
# object.var_name | BMW.model | object.method_name() | BMW.ShowModel() | 

class Cars:
    vehicle = 'car'
    
    def __init__(self, model):
        self.model = model
    
    def setprice(self, price):
        self.price = price
    
    def getprice(self):
        return self.price

BMW = Cars("X1")
BMW.setprice(120000)
print(BMW.getprice()) 

# ATTENCION: Self is a default variable that contains the memory address of the current object.
# the first argument to any object method is SELF because the first argument is always object
# reference. This process takes place automatically whether you call it or not.

class Country:
 def __init__(Myobject, a, b):
     Myobject.country = a
     Myobject.capital = b
    
 def myFunction(abc):
     print("Capital of " + abc.country + " " + "is: "+abc.capital)

r = Country("Brazil", "Brasília")
r.myFunction()

# The property object can be delete using the 'del' keyword, like: del object_name.property 
# or del object_name.

#------------------------------------------------------------------------------------------------

# Example 6: set()
# Set is a math term for a sequence consisting of distinct language is also extended in its 
# language. The set() methos is used to convert any of iterable to sequence of iterable elements
# with distinct elements, commonly called SET.

# Set() with list and tuples.

var_list = [1, 2, 3, 4, 5]
print("List before conversion: " + str(var_list))
# print("List after conversion: " + str(setattr(var_list)))

var_tuple = (5, 4, 3, 2, 1)
print("Tuple before conversion: " + str(var_tuple))
# print("Tuple after conversion: " + str(setattr(var_tuple)))







