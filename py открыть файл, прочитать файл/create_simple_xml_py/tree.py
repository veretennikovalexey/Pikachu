import xml.etree.cElementTree as et
root = et.Element( "root" )
doc = et.SubElement( root, "doc" )
et.SubElement( doc, "field1", name = "blah" ).text = "some value1"
et.SubElement( doc, "field2", name = "asdfasd" ).text = "some vlaue2"
tree = et.ElementTree( root )
tree.write( "filename.xml" )

'''
ElementTree
'''