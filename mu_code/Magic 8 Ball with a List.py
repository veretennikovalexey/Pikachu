import random
messages = [ 'it is certain', 'it is decidedly so', 'yes definitely', 'reply hazy try again',
  'ask again later', 'concentrate and ask again', 'my reply is no', 'outlook not so good', 'very doubtful' ]
magic8ball = random.randint( 0, len( messages ) - 1 )
print( messages[ magic8ball ] )    # сегодня будет зарплата ?
print( random.choice( messages ) ) # а завтра ?
