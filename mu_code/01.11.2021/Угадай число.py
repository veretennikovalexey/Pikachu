import random
загаданноеЧисло = random.randint( 1, 100 )
for попытка in range( 10 ) :
    введённоеЧисло = int( input( str( попытка ) + '> ' ) )
    if введённоеЧисло > загаданноеЧисло :
        print( 'меньше' )
    elif введённоеЧисло < загаданноеЧисло :
        print( 'больше' )
    else : break
if загаданноеЧисло == введённоеЧисло :
    print( 'угадал' )

