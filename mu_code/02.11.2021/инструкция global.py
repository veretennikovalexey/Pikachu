def spam() :
  global eggs
  eggs = 'spam'
eggs = 'global'
spam()
print( eggs ) # функция spam изменила значение переменной eggs
