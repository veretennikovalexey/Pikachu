spam = { 'color': 'red', 'age' : 42 }
print( spam.keys() )         # dict_keys( ['color', 'age'] )
print( list( spam.keys() ) ) # ['color', 'age']

######################################################

print( type( spam.values() ) ) # <class 'dict_values'>
for v in spam.values() :
  print( v, end = ' ' ) # red 42
print()

print( type( spam.keys() ) ) # <class 'dict_keys'>
for k in spam.keys() :
  print( k, end = ' ' ) # color age
print()

print( type( spam.items() ) ) # <class 'dict_items'>
for item in spam.items() :
  print( item )
# ( 'color', 'red' )
# ( 'age'  ,   42 )

print( type( item ) ) # <class 'tuple'>

for key, value in spam.items() :
  print( 'Key ' + key + ', value ' + str( value )  )

# Key color, value red
# Key   age, value  42


