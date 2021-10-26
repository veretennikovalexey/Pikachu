cost = float( input( 'Стоимость обеда составила ' ) )
tax = cost * 0.2
tip = cost * 0.1
total = cost + tax + tip
print( "Налог составил %.2f чаевые - %.2f, итого %.2f" \
  %( tax, tip, total ) )
