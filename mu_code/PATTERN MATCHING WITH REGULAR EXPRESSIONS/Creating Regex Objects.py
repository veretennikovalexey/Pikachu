import re
phoneNumRegex = re.compile( r'\d\d\d-\d\d\d-\d\d\d\d' )
print( type( phoneNumRegex ) ) # <class 're.Pattern'>
mo = phoneNumRegex.search( 'My number is 415-555-4242' )
print( type( mo ) ) # <class 're.Match'>
print( 'Phone number found: ' + mo.group() )

'''
using regular expression ( regex ) in Python

1. Import the regex module with import re
2. Create a regex object with re.compile() function ( use raw string like r'' )
3. Pass the string you want to search into the regex object's search() method
   This return a Match object
4. Call the Match object's group() method to return a string of actual matched text

https://pythex.org/
'''
