import random

def drawBoard( board ) :
  print( '   |   |' )
  print( ' ' + board[ 7 ] + ' | ' + board[ 8 ] + ' | ' + board[ 9 ] )
  print( '   |   |' )
  print( '-----------' )
  print( '   |   |' )
  print( ' ' + board[ 4 ] + ' | ' + board[ 5 ] + ' | ' + board[ 6 ] )
  print( '   |   |' )
  print( '-----------' )
  print( '   |   |' )
  print( ' ' + board[ 1 ] + ' | ' + board[ 2 ] + ' | ' + board[ 3 ] )
  print( '   |   |' )

def inputPlayerLetter() :
  letter = ''
  while not ( letter == 'Х' or letter == 'О' ) :
    print( 'введи крестик Х или нолик О' )
    letter = input().upper()
  if letter == 'Х' :
    return [ 'Х', 'О' ]   
  else :  
    return [ 'О', 'Х' ]   

def whoGoesFirst() :
  if random.randint( 0, 1 ) == 0 :
    return 'комп'
  else :
    return 'чел'

def playAgain() :
  print( 'Ещё ?' )
  return input().lower().startswith( 'д' )

def makeMove( board, letter, move ) :
  board[ move ] = letter

def isWinner( bo, le ) :
  return ( ( bo[ 7 ] == le and bo[ 8 ] == le and bo[ 9 ] == le ) or
  ( bo[ 4 ] == le and bo[ 5 ] == le and bo[ 6 ] == le ) or
  ( bo[ 1 ] == le and bo[ 2 ] == le and bo[ 3 ] == le ) or
  ( bo[ 7 ] == le and bo[ 4 ] == le and bo[ 1 ] == le ) or
  ( bo[ 8 ] == le and bo[ 5 ] == le and bo[ 2 ] == le ) or
  ( bo[ 9 ] == le and bo[ 6 ] == le and bo[ 3 ] == le ) or
  ( bo[ 7 ] == le and bo[ 5 ] == le and bo[ 3 ] == le ) or
  ( bo[ 9 ] == le and bo[ 5 ] == le and bo[ 1 ] == le ) )

def getBoardCopy( board ) :
  dupeBoard = []
  for i in board :
    dupeBoard.append( i )
  return dupeBoard

def isSpaceFree( board, move ) :
  return board[ move ] == ' '

def getPlayerMove( board ) :
  move = ' '
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree( board, int( move ) ) :
    print( 'Сделай ход ' )
    move = input() 
  return int( move )

def chooseRandomMoveFromList( board, movesList ):
  possibleMoves = []
  for i in movesList :
    if isSpaceFree( board, i ) :
      possibleMoves.append( i )
  if len( possibleMoves ) != 0 :
    return random.choice( possibleMoves )
  else :
    return None

def getComputerMove( board, computerLetter ) :
  if computerLetter == 'Х' :
    playerLetter = 'О'
  else :
    playerLetter = 'Х'
  
  for i in range( 1, 10 ) :
    copy = getBoardCopy( board )
    if isSpaceFree( copy, i ) :
      makeMove( copy, computerLetter, i )
      if isWinner( copy, computerLetter ) :
        return i

  for i in range( 1, 10 ) :
    copy = getBoardCopy( board )
    if isSpaceFree( copy, i ) :
      makeMove( copy, computerLetter, i )
      if isWinner( copy, playerLetter ) :
        return i

  move = chooseRandomMoveFromList( board, [ 1, 3, 7, 9 ] )
  if move != None :
    return move

  if isSpaceFree( board, 5 ) :
    return 5

  return chooseRandomMoveFromList( board, [ 2, 4, 6, 8 ] )

def isBoardFull( board ) :
  for i in range( 1, 10 ) :
    if isSpaceFree( board, i ) :
      return False
  return True

print( '* * *' )

while True :
  theBoard = [ ' ' ] * 10
  playerLetter, computerLetter = inputPlayerLetter()
  turn = whoGoesFirst()
  print ( 'Первым ходит ' + turn )
  gameIsPlaying = True

  while gameIsPlaying :
    if turn == 'чел' :
      drawBoard( theBoard )
      move = getPlayerMove( theBoard )
      makeMove( theBoard, playerLetter, move )
 
      if isWinner( theBoard, playerLetter ) :
        drawBoard( theBoard )     
        print( 'Ты победил !' )
        gameIsPlaying = False
      else :
        if isBoardFull( theBoard ) :
          print( 'ничья' )
          gameIsPlaying = False
          break
        else :
          turn = 'комп'

    else : # ход компа
      move = getComputerMove( theBoard , computerLetter )
      makeMove( theBoard , computerLetter, move )

      if isWinner( theBoard,computerLetter ) :
        drawBoard( theBoard )     
        print( 'ты проиграл' )
        gameIsPlaying = False
      else :
        if isBoardFull( theBoard ) :
          print( 'ничья' )
          gameIsPlaying = False
          break
        else :
          turn = 'чел'
  
  if not playAgain() :
    break
