import re
phoneNumRegex = re.compile( r'\d\d\d-\d\d\d-\d\d\d\d' )
mo = phoneNumRegex.search( 'Cell: 415-555-9999 Work: 212-555-0000' )
print( mo.group() ) # 415-555-9999

phoneNumRegex = re.compile( r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)' )
print( phoneNumRegex.findall( 'Cell: 415-555-9999 Work: 212-555-0000' ) )
# [('415', '555', '9999'), ('212', '555', '0000')]

phoneNumRegex = re.compile( r'\d\d\d-\d\d\d-\d\d\d\d' )
print( phoneNumRegex.findall( 'Cell: 415-555-9999 Work: 212-555-0000' ) )
# ['415-555-9999', '212-555-0000']


"""
\d\d\d-\d\d\d-\d\d\d\d the methon findall() returns a list of strings
[ '415-555-9999', '212-555-0000' ]

but, when you called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d)
the methon findall() returns a list of tuples of strings
[ ( '415', '555', '9999' ), ( '212', '555', '0000' ) ]
"""

'''
search() first
findall() every
'''
