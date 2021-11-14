'''
Символ ? означает, что  п р е д ш е с т в у ю щ а я  ему группа символов
необязательна
'''

import re
phoneRegex = re.compile( r'(\d\d\d-)?\d\d\d-\d\d\d\d' )
mo1 = phoneRegex.search( 'Мой номер 415-555-4242' )
print( mo1.group() ) # 415-555-4242

mo2 = phoneRegex.search( 'Мой номер 555-4242' )
print( mo2.group() ) # 555-4242

'''
Можно составить регулярное выражение которое будет находить
номера содержащие код региона и также номера не содержащие код региона
'''

batRegex = re.compile( r'Бэт(ву)?мен' )
mo1 = batRegex.search( 'Мой герой - Бэтмен' )
print( mo1.group() ) # Бэтмен

mo2 = batRegex.search( 'Мой героиня - Бэтвумен' )
print( mo2.group() ) # Бэтвумен
