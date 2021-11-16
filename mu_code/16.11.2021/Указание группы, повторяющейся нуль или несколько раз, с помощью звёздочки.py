import re

batRegex = re.compile( r'Бэт(ву)*мен')
mo1 = batRegex.search( 'Мой герой - Бэтмен' )
print( mo1.group() ) # Бэтмен

mo1 = batRegex.search( 'Моя героиня - Бэтвумен' )
print( mo1.group() ) # Бэтвумен

mo1 = batRegex.search( 'Моя героиня - Бэтвувувувумен' )
print( mo1.group() ) # Бэтвувувувумен

'''
* означает найти нулевое или большее количество экземпляров
'''
