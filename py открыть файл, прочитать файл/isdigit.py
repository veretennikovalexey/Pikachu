x = input().split()
word = ''
for ii in x :
  if len( word ) > 0 and ii.isdigit() == False :    
    print( word + ' ' + ii )
  if ii.isdigit() == False :
    word = ii
  else :
    word = ''  
  # print( ii )