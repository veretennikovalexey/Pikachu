import time, sys
indent = 0
indentIncreasing = True

try :
  while True :
    print( ' ' * indent, end = '' )
    print( '***********' )
    time.sleep( 0.01 ) # пауза 1 / 10 секунды
    if indentIncreasing :
      indent += 1
      if indent == 40 :
        indentIncreasing = False
    else :
      indent -= 1
      if indent == 0 :
        indentIncreasing = True
except KeyboardInterrupt :
  sys.exit()
