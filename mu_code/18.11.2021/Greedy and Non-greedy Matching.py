import re
greedyHaRegex = re.compile( r'(Ha){3,5}' )
mo1 = greedyHaRegex.search( 'HaHaHaHaHa' )
print( mo1.group() ) # HaHaHaHaHa

nongreedyHaRegex = re.compile( r'(Ha){3,5}?' )
mo1 = nongreedyHaRegex.search( 'HaHaHaHaHa' )
print( mo1.group() ) # HaHaHa


'''
The non-greedy ( also called lazy ) version of the braces
has the closing brace followed by question mark
It's matches the shortest string possible
Python's regular expressions are greedy by default
'''
