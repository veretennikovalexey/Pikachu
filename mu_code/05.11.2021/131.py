spam = [ 'кот', 'мышь', 'крыса', 'слон' ]
del spam[ 2 ] # spam = [ 'кот', 'мышь', 'слон' ]
del spam[ 2 ] # spam = [ 'кот', 'мышь' ]
spam[ 10000 ]

# Traceback (most recent call last):
#   File "c:\users\os\desktop\04.11.2021\127.py", line 2, in <module>
#     spam[ 10000 ]
# IndexError: list index out of range
