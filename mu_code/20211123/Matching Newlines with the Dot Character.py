import re
newlineRegex = re.compile( '.*', re.DOTALL )
aa = 'Serve the public trust\nProtect the innocent\nUphold the law'
aa = newlineRegex.search( aa ).group() # Serve the public trust
print( aa )
# Serve the public trust
# Protect the innocent
# Uphold the law

noNewlineRegex = re.compile( '.*' )
aa = 'Serve the public trust\nProtect the innocent\nUphold the law'
aa = noNewlineRegex.search( aa ).group()
print( aa ) # Serve the public trust
'''
re.DOTALL
'''
