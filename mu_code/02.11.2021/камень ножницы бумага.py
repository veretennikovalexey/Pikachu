import random, sys
wins = 0
losses = 0
ties = 0
while True :
  print( '%s побед, %s поражений, %s ничьих' \
    % ( wins, losses, ties )  )
  while True :
    playerMove = input( 'к - камень н - ножницы б - бумага в - выход : ' )
    if playerMove == 'в' :
      sys.exit()
    if playerMove == 'к' or playerMove == 'н' or playerMove == 'б' :
      break

  if playerMove == 'к' :
    print( 'камень', end = ' ' )
  if playerMove == 'н' :
    print( 'ножницы', end = ' ' )
  if playerMove == 'б' :
    print( 'бумага', end = ' ' )

  randomNumber = random.randint( 1, 3 )
  if randomNumber == 1 :
    computerMove = 'к'
    print ( 'vs камень' )
  if randomNumber == 2 :
    computerMove = 'н'
    print ( 'vs ножницы' )
  if randomNumber == 3 :
    computerMove = 'б'
    print ( 'vs бумага' )

  if playerMove == computerMove :
    print( 'ничья' )
    ties += 1
  elif playerMove == 'к' and computerMove == 'н' or \
    playerMove == 'б' and computerMove == 'к' or \
    playerMove == 'н' and computerMove == 'б' :
    print( 'победа' )
    wins += 1
  elif playerMove == 'к' and computerMove == 'б' or \
    playerMove == 'б' and computerMove == 'н' or \
    playerMove == 'н' and computerMove == 'к' :
    print( 'поражение' )
    losses += 1



