try :
  file = open( 'c:/users/os/desktop/my.txt', 'w' )
  print( u'1 Максим', file = file )
finally :
  file.close()    