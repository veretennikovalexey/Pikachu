aa = u"\
<p style = \"font-size: 22px\"> \n\
  This tag 'p' contains text, links to <a href = \"https://ru.stackoverflow.com\">stackoverflow</a>, \n\
  <a href = \"https://mail.google.com/mail/u/0/#inbox\">gmail</a> and \n\
  <a href = \"https://ya.ru/\">yandex</a> <br><br>\n\
  <a href = \"https://web.telegram.org/k\">telegram</a>                                <br><br>\n\
  <a href = \" https://web.whatsapp.com \">whatsapp</a>                                <br><br>\n\
  <a href = \" c:/users/alex/RESTful_Web_APIs_(2013).pdf \">api book</a>               <br><br>\n\
  <a href = \" https://wiki.sftserv.ru/index.php/Заглавная_страница \">Фабиус wiki</a> <br><br>\n\
  <br><br>\n\
  <br><br>\n\
</p>"
try :
  file = open( 'c:/users/alex/desktop/p.html', 'w' )
  print( aa, file = file )
finally :
  file.close() 

# <a href = \" C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code.lnk \">vscode</a> <br><br>\n\
# 