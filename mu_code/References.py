spam = 42      # spam = 42
cheese = spam  # spam = 42  cheese = 42
spam = 100     # spam = 100 cheese = 42

spam = list( '012345' ) # spam = ['0', '1', '2', '3', '4', '5']
cheese = spam  # cheese = ['0', '1', '2', '3', '4', '5']
cheese[ 1 ] = 'Hello !'
print( * spam ) # 0 Hello ! 2 3 4 5

# переменная spam изменилась, хотя мы меняли переменную cheese
