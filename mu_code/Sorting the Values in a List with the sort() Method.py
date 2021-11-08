spam = [ 2, 5, 3.14, 1, -7 ]
spam.sort()
print( * spam )  # -7 1 2 3.14 5
spam = [ 'ants', 'cats', 'dogs', 'badgers', 'elephants' ]
spam.sort()
print( * spam ) # ants badgers cats dogs elephants
spam.sort( reverse = True )
print( * spam ) # elephants dogs cats badgers ants
spam = [ 'Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats' ]
spam.sort()
print( * spam ) # Alice Bob Carol ants badgers cats
spam = [ 'a', 'z', 'A', 'Z' ]
spam.sort()
print( * spam ) # A Z a z
print()

spam.sort( key = str.lower )
print( * spam ) # A a Z z
print()

# https://wiki.python.org/moin/HowTo/Sorting
