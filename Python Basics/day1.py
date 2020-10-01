import keyword
""" 
key = ["for","while","elif","def","samriddhi","else","if"]

for i in range(len(key)):
    if keyword.iskeyword(key[i]):
       print(key[i] + " is a keyword")
    else:
        print(key[i] + " is not a keyword") 

# this prints the list of all the keywords
print(keyword.kwlist)

Output : ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#################

>>> print(None == 0)
False
>>> x = None
>>> y = None
>>> print( x == y)
True
>>> print( True or False)
True
>>> print( True and False)
False
>>> print( not False)
True
>>> print(not True)
False

x = (i for i in range(3))
for i in x:
    print(i)
for i in x:
    print(i)

"""
for i in range(10
