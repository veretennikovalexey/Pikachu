picnicItems = { 'apples': 5, 'cups': 2 }
cups = picnicItems.get( 'cups', 0 )                # сколько чашек
print( 'I am bringing ' + str( cups ) + ' cups' )
eggs = picnicItems.get( 'eggs', 0 )                # сколько яиц
print( 'I am bringing ' + str( eggs ) + ' eggs' )
