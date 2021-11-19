import re
vowelRegex = re.compile( r'[aeiouAEIOU]' )
RoboCop_eats_baby_food = 'RoboCop eats baby food. BABY FOOD!'
aa = vowelRegex.findall( RoboCop_eats_baby_food )
print( aa ) # [ 'o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O' ]

consonantRegex =  re.compile( r'[^aeiouAEIOU]' )
aa = consonantRegex.findall( RoboCop_eats_baby_food )
print( aa )

# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ',
#  'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '!' ]

'''
можно определить собственный символьный класс
используя квадратные скобки
если использовать шляпку ^ то, получится инвертированный символьный класс
'''
