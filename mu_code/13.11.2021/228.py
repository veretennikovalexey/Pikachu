'''
В регулярных выражениях следующие символы имеют специальное значение
. ^ $ * + ? { } [ ] \ | ( )

Если требуется найти их в текстовом шаблоне, нужно экранировать их
с помощью обратной косой черты
\. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)

'''

import re
re.compile( r'(\(Parentheses\)' )
#         (   (                 )   две скобки левые и только одна правая
# ( остальные скобки \( \) экранированы, это значит, что их не существует )

Traceback (most recent call last):
  File "c:\users\os\desktop\13.11.2021\228.py", line 12, in <module>
    re.compile( r'(\(Parentheses\)' )
'''
незавершенный подшаблон в позиции 0

Сообщение об ошибке говорит о том, что в позиции 0 строки r'(\(Parentheses\)'
стоит открывающая скобка, для которой отсутствует закрывающая скобка
'''
re.error: missing ), unterminated subpattern at position 0