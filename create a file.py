aa = u"Максим"
try :
  file = open( 'c:/users/os/desktop/my.txt', 'w' )
  print( aa, file = file )
finally :
  file.close()   