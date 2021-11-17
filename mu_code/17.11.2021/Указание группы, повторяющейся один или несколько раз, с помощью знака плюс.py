import re
batRegex = re.compile( r'Бэт(ву)+мен' )
mo1 = batRegex.search( 'Моя героиня - Бэтвумен' )
print( mo1.group() ) # Бэтвумен

mo1 = batRegex.search( 'Моя героиня - Бэтвувувувумен' )
print( mo1.group() ) # Бэтвувувувумен

mo1 = batRegex.search( 'Моя героиня - Бэтмен' )
print( mo1 == None ) # True

'''
+ означает 1 или больше
* означает 0 или больше
https://github.com/veretennikovalexey/Pikachu/tree/main/mu_code/16.11.2021
'''
