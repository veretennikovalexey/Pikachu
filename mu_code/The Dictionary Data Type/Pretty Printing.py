import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message :
  count.setdefault( character, 0 )
  count[ character ] = count[ character ] + 1

pprint.pprint( count )

aa = pprint.pformat( count )
# "{' ': 13,\n ',': 1,\n 'A': 1,\n 'I': 1,\n 'a': 4,\n 'b': 1,\n 'c': 3,\n
#   'd': 3,\n 'e': 5,\n 'g': 2,\n 'h': 3,\n 'i': 6,\n 'k': 2,\n 'l': 3,\n
#   'n': 4,\n 'o': 2,\n 'p': 1,\n 'r': 5,\n 's': 3,\n 't': 6,\n 'w': 2,\n 'y': 1}"

# {' ': 13,
#  ',': 1,
#  'A': 1,
#  'I': 1,
#  'a': 4,
#  'b': 1,
#  'c': 3,
#  'd': 3,
#  'e': 5,
#  'g': 2,
#  'h': 3,
#  'i': 6,
#  'k': 2,
#  'l': 3,
#  'n': 4,
#  'o': 2,
#  'p': 1,
#  'r': 5,
#  's': 3,
#  't': 6,
#  'w': 2,
#  'y': 1}
