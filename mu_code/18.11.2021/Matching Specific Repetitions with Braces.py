import re
haRegex = re.compile( r'(Ha){3}' )
mo1 = haRegex.search( 'HaHaHa' )
print( mo1.group() ) # HaHaHa

mo1 = haRegex.search( 'Ha' )
print( mo1 == None ) # True
'''
(Ha){3,5} == ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
(Ha)(Ha)(Ha) == (Ha){3}
(Ha){3,}
(Ha){,5}
(Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', 'HaHaHaHaHa'
(Ha){3} will match the string 'HaHaHa'
'''
