spam = [ 'cat', 'bat', 'rat', 'elephant' ]
spam.remove( 'bat' )
print( * spam ) # cat rat elephant
spam = [ 'cat', 'bat', 'rat', 'cat', 'hat', 'cat' ]
spam.remove( 'cat' ) # will remove only the first instance
print( * spam ) # bat rat cat hat cat

# The del statement is good to use when you know
# the index of the value you want to remove from the list
# The remove() method is useful when you know the value you want to remove from the list
