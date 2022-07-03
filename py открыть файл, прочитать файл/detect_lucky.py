def detect_lucky( number ) :
  ns = str( number )
  if int( ns[ 0 ] ) + int( ns[ 1 ] ) + int( ns[ 2 ] ) == \
    int( ns[ 3 ] ) + int( ns[ 4 ] ) + int( ns[ 5 ] ) :
    return True
  else :
    return False          
print( detect_lucky( 885778 ) )


# 985778