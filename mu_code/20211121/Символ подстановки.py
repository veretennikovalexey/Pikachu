import re
atRegex = re.compile( r'.at' )
aa = 'The cat in the hat sat on the flat mat'
aa = atRegex.findall( aa )
print( aa ) # [ 'cat', 'hat', 'sat', 'lat', 'mat' ]
'''
Любой одиночный символ за исключением символа новой строки
.
'''
