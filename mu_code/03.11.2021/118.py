def spam( divideBy ) :
  try :
    return 42 / divideBy
  except ZeroDivisionError :
    print( 'На ноль делить нельзя' )
  except :
    print( 'Произошло исключение' )

print( spam( 0 ) )

# На ноль делить нельзя
# None
