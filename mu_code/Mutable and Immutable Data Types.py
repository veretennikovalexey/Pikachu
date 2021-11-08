eggs = [ 1, 2, 3 ]
print( * eggs )
del eggs[ 2 ]
print( * eggs )
del eggs[ 1 ]
print( * eggs )
del eggs[ 0 ]
print( * eggs )
eggs.append( 4 )
print( * eggs )
eggs.append( 5 )
print( * eggs )
eggs.append( 6 )
print( * eggs )

# 1 2 3
# 1 2
# 1

# 4
# 4 5
# 4 5 6

# всё те же яйца

