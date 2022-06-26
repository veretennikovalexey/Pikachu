import random, sys
print( 'камень, ножницы, бумага' )
wins = 0
loss = 0
ties = 0
while True :
  print( f' { wins } { loss } { ties }' )
  while True :
    print( 'к н б или в' )
    playerMove = input()
    if playerMove == 'в' :
      sys.exit()
    if playerMove == 'к' or playerMove == 'н' or playerMove == 'б' :
      break
    print( '-------------> к н б или в' )
  if playerMove == 'к' :
    print( 'Вы выбрали камень' )
  if playerMove == 'н' :
    print( 'Вы выбрали ножницы' )
  if playerMove == 'б' :
    print( 'Вы выбрали бумагу' )

  rand = random.randint( 1, 3 )
  if rand == 1 :
    compMove = 'к'
    print( 'Компьютер выбрал камень' )  
  if rand == 2 :
    compMove = 'н'
    print( 'Компьютер выбрал ножницы' )  
  if rand == 3 :
    compMove = 'б'
    print( 'Компьютер выбрал бумагу' )  

  if playerMove == compMove :
    print( 'ничья' )
    ties = ties + 1
  if playerMove == 'к' and compMove == 'н' :
    print( 'Камень ломает ножницы' ) 
    wins = wins + 1
  if playerMove == 'б' and compMove == 'к' :
    print( 'Бумага заворачивает камень' ) 
    wins = wins + 1
  if playerMove == 'н' and compMove == 'б' :
    print( 'Ножницы режут бумагу' ) 
    wins = wins + 1

  if compMove == 'к' and playerMove == 'н' :
    print( 'Ваши ножницы сломаны' ) 
    loss = loss + 1
  if compMove == 'б' and playerMove == 'к' :
    print( 'Ваш камень завёрнут' ) 
    loss = loss + 1
  if compMove == 'н' and playerMove == 'б' :
    print( 'Ваша бумага разрезана' ) 
    loss = loss + 1