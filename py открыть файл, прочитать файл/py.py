passwordFile = open( 'SecretPasswordFile.txt' )
secretPassword = passwordFile.read()
print( secretPassword )
typedPassword = input()
if typedPassword == secretPassword :
    print( 'Доступ разрешён' )
    if typedPassword == '12345':
        print( 'Пожалуйста, установите новый пароль' )
else :
    print( 'Вы ввели неверный пароль' )
