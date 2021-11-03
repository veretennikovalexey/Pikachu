def spam() :
  print( eggs ) # ошибка
  eggs = 'spam local'

eggs = 'global'
spam()

# Traceback (most recent call last):
#   File "c:\users\os\desktop\03.11.2021\116.py", line 6, in <module>
#     spam()
#   File "c:\users\os\desktop\03.11.2021\116.py", line 2, in spam
#     print( eggs ) # ошибка
# UnboundLocalError: local variable 'eggs' referenced before assignment
#
# Локальная переменная упоминается перед назначением ( присваиванием )
