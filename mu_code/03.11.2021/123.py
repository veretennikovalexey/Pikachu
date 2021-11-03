def collatz( number ) :
  if number % 2 == 0 : # чётное
    result = number // 2
  if number % 2 == 1 : # нечётное
    result = 3 * number + 1
  print( result )
  return result

error = True
while error :
  error = True
  try :
    num = int( input( 'Введите число больше нуля: ' ) )
    if num > 0 :
      error = False
  except :
    error = True

firstTime = True
while num != 1 or firstTime :
  firstTime = False
  num = collatz( num )

# если number - чётное, тогда это число надо разделить на 2 без остатка
