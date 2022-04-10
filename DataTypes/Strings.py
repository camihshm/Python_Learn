#----------------------------------------------------------------------------------
## Data Type: Strings.
## The data type string characteristics: 
## - Sequences of character data.
## - In python string is called = str.
## - Can be use with (' ') or (" ").
## - The format include raw or triple-quoted strings. 
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Example 1: Strings types, you can use (' ') or (" ").
#----------------------------------------------------------------------------------

name = 'My name is Camila.'
print(name)

name = "My name is Camila."
print(name)

#----------------------------------------------------------------------------------
# Example 2: But be careful with words have (') like wasn't, don't, she's and etc.
#----------------------------------------------------------------------------------

Person1 = "Hey Lucas, what's up?"
print(Person1)

# The wrong way to use (' '). In this case, you can use (" ")
# Person2 = 'Hi Cami, I'm great! What are you doing here?'
# print(Person2)

Person2 = "Hi Cami, I'm great! What are you doing herer?"
print(Person2)

Person1 = "I'm visiting my family and you?"
print(Person1)

Person2 = "Awesome! I'm just pass from you hehehe. See you Cami!"
print(Person2)

Person1 = "Bye Lucas."
print(Person1)

#----------------------------------------------------------------------------------
# Suppressing Special Character Meaning
#----------------------------------------------------------------------------------
# Escape    | Usual Interpretation of Character(s)   | "Escaped"
# Sequence  | After Backslash                        | Interpretation
#----------------------------------------------------------------------------------
# \'        | Terminates string with single quote    | Literal single quote (')
#           | opening delimiter                      | character
#----------------------------------------------------------------------------------
# \"        | Terminates string with double quote    | Literal double quote (")
#           | opening delimiter                      | character
#----------------------------------------------------------------------------------
# \<newline>| Terminates                             | Newline is
#           | input line                             | ignored
#----------------------------------------------------------------------------------
# \\        | Introduce escape                       | Literal backslash (\)
#           | sequence                               | character
# #----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Example 3: Ways to break up string over lines.
#----------------------------------------------------------------------------------

# Break up over more than one line, include a backslash before each newline and the 
# newlines will be ignored:
print('a\
b\
c')

# To include a literal backslash in a string, escape it with a backslash:
print ('foo\\bar')

#----------------------------------------------------------------------------------
# Applying Special Meaning to Characters
#----------------------------------------------------------------------------------
# In python and almost all other common computer languages a tab character can be
# specified by the escape sequence : \t. 
# The escape sequence \t causes the t character to lose its usual meaning, 
# that of a literal t. Instead, the combination is interpreted as a tab character.
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Escape Sequence    | "Escaped" Interpretation
#----------------------------------------------------------------------------------
# \a                 | ASCII Bell(BEL) character
#----------------------------------------------------------------------------------
# \b                 | ASCII Backspace(BS) character
#----------------------------------------------------------------------------------
# \f                 | ASCII Formfeed(FF) character
#----------------------------------------------------------------------------------
# \n                 | ASCII Linefeed(LF) character
#----------------------------------------------------------------------------------
# \N{<name>}         | Character from Unicode database with given <name>
#----------------------------------------------------------------------------------
# \r                 | ASCII Carriage Return(CR) character
#----------------------------------------------------------------------------------
# \t                 | ASCII Horizontal Tab(TAB) character
#----------------------------------------------------------------------------------
# \uxxxx             | Unicode character with 16-bit hex value xxxx
#----------------------------------------------------------------------------------
# \Uxxxxxxxx         | Unicode character with 32-bit hex value xxxxxxxx
#----------------------------------------------------------------------------------
# \v                 | ASCII Vertical Tab(VT) character
#----------------------------------------------------------------------------------
# \ooo               | Character with octal value ooo
#----------------------------------------------------------------------------------
# \xhh               | Character with hex value hh
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Examples - This type of escape sequence is typically used to insert characters 
# that are not readily generated from the keyboard or are not easily readable 
# or printable.
#----------------------------------------------------------------------------------

a = "a\tb"
print(a)

b = "a\141\x61"
print(b)

c = "a\nb"
print(c)

d = '\u2192 \N{rightwards arrow}'
print(d)

#----------------------------------------------------------------------------------
# Raw Strings - literal is proceded by r or R, which specifies that escape 
# sequences in the associated string are not translated. The backslash character
# is left in the string.
#----------------------------------------------------------------------------------

A = 'foo\nbar'
print(A)

print(r'foo\nbar')

C = 'foo\\bar'
print(C)

print(R'foo\\bar')

#----------------------------------------------------------------------------------
# Triple-Quoted Strings - there is yet another way of delimiting strings in Python. 
# Triple-quoted strings are delimited by matching groups of three single quotes or 
# three double quotes. Escape sequences still work in triple-quoted strings, 
# but single quotes, double quotes, and newlines can be included without escaping 
# them. This provides a convenient way to create a string with both 
# single and double quotes in it.
#----------------------------------------------------------------------------------

v = '''This string have a single (') and double (") quote.'''
print(v)

v = """This string have a single (') and double (") quote."""
print(v)