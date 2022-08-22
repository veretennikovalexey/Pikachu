from lxml import etree
tree = etree.parse( "WayBill.xml" )
root = tree.getroot() # Documents
ns = root.nsmap
consignee = root.find( './/wb:Consignee', ns ) 
name = consignee.find( ".//oref:ShortName", ns )
print( name.text )