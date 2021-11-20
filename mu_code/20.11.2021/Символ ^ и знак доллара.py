import re
wholeStringIsNum = re.compile( r'^\d+$' )
aa = '0123456789'
aa = wholeStringIsNum.search( aa ) # <re.Match object; span=(0, 10), match='0123456789'>
print( aa )
print( wholeStringIsNum.search( '12x34' ) ) # None
print( wholeStringIsNum.search( '12 34' ) ) # None

endsWithNumber = re.compile( r'\d$' )
aa = 'Ваше число - 42'
aa = endsWithNumber.search( aa ) # <re.Match object; span=(14, 15), match='2'>
print( aa )

beginsWithHello = re.compile( r'^Здравствуй' )
aa = 'Здравствуй, мир!'
aa = beginsWithHello.search( aa )
print( aa ) # <re.Match object; span=(0, 10), match='Здравствуй'>
print( beginsWithHello.search( ' Здравствуй ' ) ) # None

'''
Если поставить символ ^ ( карет ) то будет произведён поиск в начале текста
Если поставить символ $ ( доллар ) то будет произведён поиск в конце текста
Также можно использовать оба символа одновременно
'''
