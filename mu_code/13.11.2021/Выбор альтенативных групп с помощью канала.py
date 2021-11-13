import re
batRegex = re.compile( r'Бэт(мэн|мобиль|коптер|бэт)' )
mo = batRegex.search( 'Бэтмобиль потерял колесо' )
print( mo.group() ) # Бэтмобиль
print( mo.group( 1 ) ) # мобиль

"""
Символ | в регулярном выражении называется каналом ( pipe )
Его надо использовать, когда у нас имеется несколько вариантов поиска
Например,

'Бэтман|Тина Фей'
"""

heroRegex = re.compile( r'Бэтмен|Тина Фей' )
mo1 = heroRegex.search( 'Бэтмен и Тина Фей' )
print( mo1.group() ) # Бэтмен

mo2 = heroRegex.search( 'Тина Фей и Бэтмен' )
print( mo2.group() ) # Тина Фей

mo3 = heroRegex.findall( 'Бэтмен Бэтмен Тина Фей' )
print( * mo3 ) # Бэтмен Бэтмен Тина Фей


