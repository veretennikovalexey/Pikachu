import random
pets = [ 'dog', 'cat', 'moose' ] # собака кошка лось
print( random.choice( pets ) )   # случайный выбор
people = [ 'Alice', 'Bob', 'Carol', 'David' ] # ABCD
random.shuffle( people ) # Перемешивание
print( * people )        # Alice Carol David Bob
