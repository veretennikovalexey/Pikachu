'''
Review of regex symbols

?     zero or one of the preceding group
*     zero or more of the preceding group
+     one or more of the preceding group
{n}   exacltly n of the preceding group
{n,}  n or more of the preceding group
{,m}  0 to m of the preceding group
{n,m} matches at least n and at most m of the preceding group
{n,m}? or *? or +? perfoms a non-greedy match of the preceding group
^spam string must begin with spam
spam$ string must end with spam
.     any character, except newline
\d    a digit
\w    word
\s    space
\D    anything except a digit
\W    anything except word character
\S    anything except space character
[abc] matches any charecter between the brackers ( such as a,b or c )
[^abc] matches any charecter that isn't between the brackets
'''
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
