# def

def convert_co_cels( fahren ) :

    return ( fahren - 32 ) * 5 / 9

# idle shell

import os # Подключаем модуль 

os.chdir( 'c:\\fabius\\idle' )

try :

  file = open( 'my.txt', 'w' )
  
finally :

  file.close()
  
