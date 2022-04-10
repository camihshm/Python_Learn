#----------------------------------------------------------------------------------
## Data Type: Integers.
## The data type interger characteristics: 
## - Whole numbers
## - Any length allowed up to memory limit of your computer.
## - Default is decimal (base 10).
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Example 1: Numbers.
#----------------------------------------------------------------------------------

x = 1
print(x)
# result = 1

y = 2
print(y)
# result = 2

z = 1000000000000000000
print(z)
# result = 1000000000000000000

w = -2
print(w)
# result = -2

#----------------------------------------------------------------------------------
# Operations maths using the variables above.
# Important: you can't concatenate value int.
#----------------------------------------------------------------------------------

SUM = x + y + z + w
print(SUM)    

SUB = x - y - z - w
print(SUB)

DIV = w / x
print (DIV)

MTL = x*z
print (MTL)

#----------------------------------------------------------------------------------
# Base(10) = Default | Base(2) = Binary | Base(8) = Octal | Base(16) = Hexadecimal
#----------------------------------------------------------------------------------
# String                             | Representation | Base
# 0b (zero + lowercase letter 'b')   | Binary         | 2
# 0B (zero + uppdercase letter 'B')  | Binary         | 2
# ---------------------------------------------------------------------------------
# 0o (zero + lowercase letter 'o')   | Octal          | 8
# 0O (zero + uppdercase letter 'O')  | Octal          | 8
# ---------------------------------------------------------------------------------
# 0x (zero + lowercase letter 'x')   | Hexadecimal    | 16
# 0X (zero + uppdercase letter 'X')  | Hexadecimal    | 16
# ---------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Example base(2) = Binary.
#----------------------------------------------------------------------------------
base_binary = 0b10
print(base_binary)

#----------------------------------------------------------------------------------
# Example base(8) = Octa.
#----------------------------------------------------------------------------------
base_octa = 0o10
print(base_octa)

#----------------------------------------------------------------------------------
# Example base(16) = Hexadecimal.
#----------------------------------------------------------------------------------
base_hexa = 0x10
print(base_hexa)


# Important: To execute this script you can download this path on your computer and
# open this file using terminal or any IDE, use the command: python Integers.py
# the terminal gonna print all the result.





