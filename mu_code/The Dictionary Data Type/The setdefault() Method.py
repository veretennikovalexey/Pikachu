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
