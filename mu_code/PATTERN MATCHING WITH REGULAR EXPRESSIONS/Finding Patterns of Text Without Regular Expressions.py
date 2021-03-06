def isPhoneNumber( text ) :
  if len( text ) != 12 :
    return False
  for ii in range( 0, 3 ) :
    if not text[ ii ].isdecimal() :
      return False
  if text[ 3 ] != '-' :
    return False
  for ii in range( 4, 7 ) :
    if not text[ ii ].isdecimal() :
      return False
  if text[ 7 ] != '-' :
    return False
  for ii in range( 8, 12 ) :
    if not text[ ii ].isdecimal() :
      return False

  return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
for ii in range ( len( message ) ) :
  chunk = message[ ii : ii + 12 ]
  if isPhoneNumber( chunk ) :
    print( 'Phone number found: ' + chunk )
print( 'Done' )

print( 'Is 415-555-4242 a phone number ?' )
print( isPhoneNumber( '415-555-4242' ) )
print( 'Is Moshi moshi a phone number ?' )
print( isPhoneNumber( 'Moshi moshi' ) )
'''
isPhoneNumber()

Проверка, является ли текст телефонным номером США
'''
