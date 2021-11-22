import re
nameRegex = re.compile( r'First Name: (.*) Last Name: (.*)' )
mo = nameRegex.search( 'First Name: Al Last Name: Sweigart' )
print( mo.group( 1 ) ) # Al
print( mo.group( 2 ) ) # Sweigart

