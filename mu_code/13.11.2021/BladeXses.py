mylist = list( '1' )
mylist2 = [ '0' ]
mylist2.append( mylist )
print( mylist2 ) # [ '0', ['1'] ]
mylist2 = [ '0' ]
mylist2.extend( mylist )
print( mylist2 ) # [ '0', '1' ]
