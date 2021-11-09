def totalBrought( guests, item ) :
  numBrought = 0
  for key, value in guests.items() :
    numBrought = numBrought + value.get( item, 0 )
  return numBrought

allGuests = {}
allGuests[ 'Alice' ] = { 'apples': 5, 'pretzels': 12 }
allGuests[ 'Bob' ] = { 'ham sandwiches': 3, 'apples': 2 }
allGuests[ 'Carol' ] = { 'cups': 3, 'apple pies': 1 }

print( 'Number of things being brought' )

cups = str( totalBrought( allGuests, 'cups' ) )
cakes = str( totalBrought( allGuests, 'cakes' ) )
apples = str( totalBrought( allGuests, 'apples' ) )
apple_pies = str( totalBrought( allGuests, 'apple pies' ) )
ham_sandwiches = str( totalBrought( allGuests, 'ham sandwiches' ) )

print( ' - Apples         ' + apples )
print( ' - Cups           ' + cups )
print( ' - Cakes          ' + cakes )
print( ' - Ham Sandwiches ' + ham_sandwiches )
print( ' - Apple Pies     ' + apple_pies )
