spam = { 'name': 'Pooka', 'age': 5 }
if 'color' not in spam :
  spam[ 'color' ] = 'black'
print( spam ) # { 'name': 'Pooka', 'age': 5, 'color': 'black' }

spam = { 'name': 'Pooka', 'age': 5 }
spam.setdefault( 'color', 'black' )
print( spam ) # { 'name': 'Pooka', 'age': 5, 'color': 'black' }

spam.setdefault( 'color', 'white' )
print( spam ) # { 'name': 'Pooka', 'age': 5, 'color': 'black' }

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message :
  count.setdefault( character, 0 )
  count[ character ] = count[ character ] + 1

print( count )

# { 'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1,
#   'r': 5, 'i': 6, 'g':  2, 'h': 3, 'c': 3, 'o': 2, 'l': 3,
#   'd': 3, 'y': 1, 'n':  4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2 }
