myPets = [ 'Софи', 'Питер', 'Толстяк' ]
name = input( 'Укажите имя моего кота или кошки: ' )
if name not in myPets :
  print( f'У меня нет кота или кошки по имени "{ name }"' )
  # print( 'У меня нет кота или кошки по имени "%s"' % name )
  # оператор интерполяции строки
elif name in [ 'Питер', 'Толстяк' ] :
  print( f'Верно, моего кота зовут { name }' )
else :
  print( 'Да, правильно, %s - моя любимая кошечка' % name )