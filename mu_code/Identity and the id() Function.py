bacon = 'Hello'
numericMemoryAddress = id( bacon )
print( numericMemoryAddress )

bacon += ' world!'
newnumericMemoryAddress = id( bacon )
print( newnumericMemoryAddress )

# 6324144
# 8003696   разные адреса

eggs = [ 'cat', 'dog' ]
numericMemoryAddress = id( eggs )
print( numericMemoryAddress )

eggs.append( 'moose' )
numericMemoryAddress = id( eggs )
print( numericMemoryAddress )

# 5958912
# 5958912   одинаковые адреса

eggs = [ 'bat', 'rat', 'cow' ]
numericMemoryAddress = id( eggs )
print( numericMemoryAddress )

# 5959168   новый адрес





