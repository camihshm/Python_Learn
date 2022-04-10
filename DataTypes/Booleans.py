#----------------------------------------------------------------------------------
## Data Type: Booleans.
## The data type booleans characteristics: 
## - Have two values: true or false.
## - False is equivalent = 0 and True is equivalent to any non-zero number.
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Example 1: Variable with true or false values.
#----------------------------------------------------------------------------------

x = True
print('My name is Camila', x)

x = 1
print(bool(x))

y = False
print('I have 24 years old', y)

y = 0
print(bool(y))

#----------------------------------------------------------------------------------
# Example 1: Booleans Truthiness.
#----------------------------------------------------------------------------------

t = bool(1)
f = bool(0)

a = 24
b = 32

if a == 24:
    print(t)
else:
    print(f)
    
if a == b:
    print(t)
else:
    print(f)




