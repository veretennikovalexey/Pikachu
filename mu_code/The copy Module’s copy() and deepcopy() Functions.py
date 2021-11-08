import copy
spam = list( 'ABCD' )
print( id( spam ) )           # 27200
cheese = copy.copy( spam )
print( id( cheese ) )         # 51904
cheese[ 1 ] = 42
print( * spam )    # A B C D
print( * cheese )  # A 42 C D


