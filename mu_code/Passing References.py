def eggs( someParameter ) :
  someParameter.append( 'Hello' )

spam = list( '123' )
eggs( spam )
print( * spam ) # 1 2 3 Hello
