import re
xmasRegex = re.compile( r'\d+\s\w+' )
aa = xmasRegex.findall( '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,\
 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge' )
print( aa )

# [ '12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans',
#   '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge' ]

'''
[0-5] == (0|1|2|3|4|5)
\d (0|1|2|3|4|5|6|7|8|9)

Shorthand codes for common character classes
\d Any numeric digit from 0 to 9
\D Any character that is not a numeric digit from 0 to 9
\w Any letter, numeric digit, or the underscore character
   ( think of this as matching word characters )
\W Any character that is not a letter, numeric digit, or the underscore character
\s Any space, tab, or newline character
   ( think of this as matching space characters )
\S Any character that is not a space, tab, or newline
'''
