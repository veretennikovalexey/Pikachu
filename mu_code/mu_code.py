passwordFile = open( 'SecretPasswordFile.txt' )
secretPassword = passwordFile.read()
print( 'Введите пароль' )
typedPassword = input()
if typedPassword == secretPassword :
  print( 'Доступ разрешён' )
  if typedPassword == '123' :
    print( 'Слишком простой пароль' )
else :
  print( 'Доступ запрещён' )
