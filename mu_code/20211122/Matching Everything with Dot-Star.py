import re
nongreedyRegex = re.compile( r'<.*?>' )
mo = nongreedyRegex.search( '<To serve man> for dinner>' )
print( mo.group() ) # <To serve man>
greedyRegex = re.compile( r'<.*>' )
mo = greedyRegex.search( '<To serve man> for dinner>' )
print( mo.group() ) # <To serve man> for dinner>
'''
the dot - star uses greedy mode
the dot - star - and - question uses non-greedy mode
'''
nameRegex = re.compile( r'First Name: (.*) Last Name: (.*)' )
mo = nameRegex.search( 'First Name: Al Last Name: Sweigart' )
print( mo.group( 1 ) ) # Al
print( mo.group( 2 ) ) # Sweigart

