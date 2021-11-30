# requests

import requests

payload = { 'website': 'heihei.ru', 'established': 2018 }

r = requests.post( 'https://httpbin.org/post', data = payload )

r_dict = r.json()

print( r_dict[ 'form' ] )

print( r_dict )

# print( f'url: { r.url } \n \ntext: \n { r.text } ' )

# split

Разделяет строку на список значений, наример, '3 20 100' -> [ '3', '20', '100' ]

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
  
