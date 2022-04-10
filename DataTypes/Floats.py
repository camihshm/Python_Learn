#----------------------------------------------------------------------------------
## Data Type: Floats.
## The data type float point numbers characteristics: 
## - Any number with a decimal point.
## - Division operations results will be a float. 
## - Can be defined usign scientific notation (2x10²=200).
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Example 1 - How attribute a float value for variables.
#----------------------------------------------------------------------------------

x = 2.5
print('value', x)

y = 3.0
print('value', y)

z = 2.500
print('value', z)

#----------------------------------------------------------------------------------
# Example 1 - Math operations with float values.
#----------------------------------------------------------------------------------

SUM = x + y + z
print('SUM', SUM)

SUB = z - y - x
print('SUB', SUB)

MTL = z*y
print('MTL', MTL)

#----------------------------------------------------------------------------------
# Example 2 - The math operation = division always results a float numbers 
# even the result is integer. For round the result you can use '//'.
# Important: is recommended using '//' only situations you need round the result. 
# Because this can modify the result when he is not a integer.
#----------------------------------------------------------------------------------

DIV = z/x
print('DIV', DIV)

DIV = y/x
print('DIV', DIV)    

#----------------------------------------------------------------------------------
# Example 3 - It's possible define numbers usign scientifc notation. 
# The scientific notation in general is a number in beginning and then the second
# part will be the powers of 10 which are applied to that number.
#----------------------------------------------------------------------------------

x = .4e7
print('x', x)

y = 4.2e-4
print('y', y)

# This scientific notation: (2x10²=200), can be declare like this:

w = 2e2
print('Positive', w)

w = 2e-2
print('Negative', w)

