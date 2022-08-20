import xml.etree.cElementTree as et
tree = et.parse( "filename.xml" )
root = tree.getroot()
doc = root.find( 'doc' )
for child in doc :
  print( child.tag, child.attrib, child.text )
'''
  field1 {'name': 'blah'   } some value1
  field2 {'name': 'asdfasd'} some vlaue2
'''

'''
  <root>
    <doc>
      <field1 name="blah">some value1</field1>
      <field2 name="asdfasd">some vlaue2</field2>
    </doc>
  </root>
'''




