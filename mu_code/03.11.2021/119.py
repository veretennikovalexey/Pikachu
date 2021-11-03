def spam( divideBy ) :
  return 42 / divideBy

try :
  print( 'В этой программе произошло исключение' )
  print( spam( 0 ) )
except ZeroDivisionError :
  print( 'На ноль делить нельзя' )

# В этой программе произошло исключение
# На ноль делить нельзя
