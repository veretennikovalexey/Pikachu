spam = [ 'cat', 'dog', 'bat' ]
spam.append( 'moose' ) # aadd
print( * spam ) # cat dog bat moose
spam.insert( 1, 'chicken' ) # это операция возвращает None
print( * spam ) # cat chicken dog bat moose
