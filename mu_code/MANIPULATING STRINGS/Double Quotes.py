# import pyperclip

# I recommend watching Ned Batchelder’s 2012 PyCon talk
# “Pragmatic Unicode, or, How Do I Stop the Pain?” at https://youtu.be/sgHbC6udIqc

print( chr( ord( 's' ) ) ) # s
print( chr( ord( 's' ) + 1 ) ) # t

print( ord( 'A' ) < ord( 'B' ) ) # True
print( ord( 'А' ) ) # 1040 - это русска буква А
print( ord( 'Я' ) ) # 1071
print( ord( 'B' ) ) # 66

print( chr( 65 ) ) # A - это английская буква А
print( ord( '!' ) ) # 33
print( ord( '4' ) ) # 52
print( ord( 'A' ) ) # 65

# ord() and chr()

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print( spam.strip( 'ampS' ) ) # BaconSpamEggs  тут убираются буквы S p a m слева и справа
spam = '           Hello, world !            '
print( spam.strip() ) # Hello, world !
print( spam.lstrip() + '.' ) # Hello, world !            .
print( spam.rstrip() ) #            Hello, world !

def printPicnic( itemsDict, leftWidth, rightWidth ) :
  print( ' PICNIC ITEMS '.center( leftWidth + rightWidth, '-' ) )
  for key, value in itemsDict.items() :
    print( key.ljust( leftWidth, '.' ) + str( value ).rjust( rightWidth ) )

picnicItems = { 'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000 }

printPicnic( picnicItems, 12, 6 )
printPicnic( picnicItems, 20, 6 )

# https://autbor.com/picnictable/

print( 'Hello'.center( 20, '=' ) ) # =======Hello========
print( 'Hello'.center( 20 ) ) #        Hello
print( 'Hello'.ljust( 20, '-' ) ) # Hello---------------
print( 'Hello'.rjust( 20, '*' ) ) # ***************Hello
print( 'Hello'.ljust( 10 ) + '#' )  # Hello     # добавляются пробелы справа, выравнивается слева
print( 'Hello, World'.rjust( 10 ) ) # Hello, World
print( 'Hello, World'.rjust( 20 ) ) #        Hello, World
print( 'Hello'.rjust( 20 ) ) #               Hello
print( 'Hello'.rjust( 10 ) ) #     Hello

before, sep, after = 'Hello, world !'.partition( ' ' )
print( after + '|' + sep + '|' + before ) # world !| |Hello,

print( 'Hello, world !'.partition( 'XYZ' ) ) # ( 'Hello, world !', '', '' )
print( 'Hello, world !'.partition( 'o' ) ) # ( 'Hell', 'o', ', world !' )
print( 'Hello, world !'.partition( 'world' ) ) # ( 'Hello, ', 'world', ' !' )
print( 'Hello, world !'.partition( 'w' ) ) # ( 'Hello, ', 'w', 'orld !' )

spam = '''Dear Alice,
How have you been ? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment"

Please do not drink it
Sincerely,
Bob'''
print( spam.split( '\n' ) )
# ['Dear Alice,',
#  'How have you been ? I am fine.',
#  'There is a container in the fridge',
#  'that is labeled "Milk Experiment"',
#  '',
#  'Please do not drink it', 'Sincerely,', 'Bob']

print( 'My name is Simon'.split( 'm' ) ) # [ 'My na', 'e is Si', 'on' ]
print( 'MyABCnameABCisABCSimon'.split( 'ABC' ) ) # [ 'My', 'name', 'is', 'Simon' ]
print( 'My name is Simon'.split() ) # [ 'My', 'name', 'is', 'Simon' ]

print( ', '.join( [ 'cats', 'rats', 'bats' ] ) )       # cats, rats, bats
print( ' '.join( [ 'My', 'name', 'is', 'Simon' ] ) )   # My name is Simon
print( 'ABC'.join( [ 'My', 'name', 'is', 'Simon' ] ) ) # MyABCnameABCisABCSimon

print( 'Hello, world !'.startswith( 'Hello' ) ) # True
print( 'Hello, world !'.endswith( 'world !' ) ) # True
print( 'abc123'.startswith( 'abcdef' ) ) # False
print( 'abc123'.endswith( '12' ) )       # False
print( 'Hello, world !'.startswith( 'Hello, world !' ) ) # True
print( 'Hello, world !'.endswith( 'Hello, world !' ) )   # True

# https://autbor.com/validateinput/

while True :
  print( 'Enter your age' )
  age = input()
  if age.isdecimal() :
    break
  print( 'Please enter a number for your age' )

while True :
  print( 'Select a new password ( letters and numbers only ): ' )
  password = input()
  if password.isalnum() :
    break
  print( 'Passwords can only have letters and numbers')

print( 'hello'.isalpha() )    # True
print( 'hello123'.isalpha() ) # False
print( 'hello123'.isalnum() )               # True
print( 'hello'.isalnum() )                  # True
print( '123'.isdecimal() )                  # True
print( '123.'.isdecimal() )                 # False
print( '    '.isspace() )                   # True
print( 'This Is Title Case'.istitle() )     # True
print( 'This Is Title Case 123'.istitle() ) # True
print( 'This Is not Title Case'.istitle() ) # False
print( 'This Is NOT Title Case Either'.istitle() ) # False


# isalpha() return True if the string consists only of letters and isn't blank
# isalnum() return True if the string consists only of letters and numbers and is not blank
# isdecimal() return True if the string consists only of numbers and is not blank
# isspace() return True if the string consists only of space, tabs, and newlines and is not blank
# istitle() return True if the string consists only of words that begin with an uppercase
#           letter followed by only lowercase letters

print( 'Hello'.upper() ) # HELLO
print( 'Hello'.upper().lower() ) # hello
print( 'Hello'.upper().lower().upper() ) # HELLO
print( 'HELLO'.lower() ) # hello
print( 'HELLO'.lower().islower() ) # True

spam = 'Hello, world !'
print( spam.islower() )    # False
print( spam.isupper() )    # False
print( 'HELLO'.isupper() ) # True
print( 'abc12345'.islower() ) # True
print( '12345'.islower() ) # False
print( '12345'.isupper() ) # False

# https://autbor.com/convertlowercase/
print( 'How are you ?' )
feeling = input()
if feeling.lower() == 'great' :
  print( 'I feel great too' )
else :
  print( 'I hope the rest of your day is good' )

spam = 'Hello, world !'
print( spam.upper() ) # HELLO, WORLD !
print( spam.lower() ) # hello, world !

name = 'Al'
age = 4000
print( 'Hello, my name is ' + name + '. I am ' + str( age ) + ' years old ' )
# Hello, my name is Al. I am 4000 years old
# string interpolation
print( 'My name is %s. I am %s years old' % ( name, age ) )
# My name is Al. I am 4000 years old
print( f'My name is { name }. Next year I will by { age + 1 }' )
# My name is Al. Next year I will by 4001
print( 'My name is { name }. Next year I will by { age + 1 }' )
# print( f'My name is { name }. Next year I will by { age + 1 }' )

print( 'Hello' in 'Hello, World' ) # True
print( 'Hello' in 'Hello' )        # True
print( 'HELLO' in 'Hello, World' ) # False
print( '' in 'spam' )              # True
print( 'cats' not in 'cats and dogs' ) # False

spam = 'Hello, world!'
print( spam[ 0 ] ) # H
print( spam[ 4 ] ) # o
print( spam[ -1 ] ) # !
flizz = spam[ 0 : 5 ]
print( flizz ) # Hello
print( spam[ : 5 ] ) # Hello
print( spam[ 7 : ] ) # Hello

'''
' H e l l o ,   w o r  l  d  ! '
  0 1 2 3 4 5 6 7 8 9 10 11 12
'''

def spam() :
  """This is a multiline comment to help
  explain what the spam() fuction does"""
  print( 'Hello !' )

"""This is a test Python program
written by al sweigart al@inventwithpython.com


This program was designed for Python 3, not Python 2
"""

spam = "That is Alice's cat"
print( spam )                        # That is Alice's cat
# escape character ( backslash \ )
spam = 'Say hi to Bob\'s mother'
print( spam )                        # Say hi to Bob's mother

# \' Single quote
# \" Double quote
# \t Tab
# \n Newline ( line break )
# \\ Backslash

print( ' Hello there ! \n How are you ? \n I\'m doing fine' )

# Hello there !
# How are you ?
# I'm doing fine

print( r'That is Carol\'s cat' )     # That is Carol\'s cat

print( '''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary and extortion

Sincerely, Bob ''' )

print( 'Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary\
 and extortion.\n\nSincerely,\nBob' )
