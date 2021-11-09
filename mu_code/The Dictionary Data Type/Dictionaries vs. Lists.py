spam = [ 'cats', 'dogs', 'moose' ]
bacon = [ 'dogs', 'moose', 'cats' ]
print( spam == bacon ) # False

eggs = { 'name': 'Zophie', 'species': 'cat', 'age': '8' }
ham = { 'species': 'cat', 'age': '8' , 'name': 'Zophie' }
print( eggs == ham ) # True

birthdays = { 'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4' }
while True :
  print( 'Enter a name: ( blank to quit )' )
  name = input()
  if name == '' :
    break
  if name in birthdays :
    print( birthdays[ name ] + ' is the birstday of ' + name )
  else :
    print( 'I do not have birthday information for ' + name )
    print( 'What is their birstday ?' )
    bday = input()
    birthdays[ name ] = bday # Сохраняем день рождения
    print( 'Birthday database updated' )
