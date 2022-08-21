from lxml import etree
tree = etree.parse( "WayBill.xml" )
root = tree.getroot() # Documents
ns = root.nsmap
doc = root.find( "ns:Document", ns ) 
wb = doc.find( "ns:WayBill_v4", ns ) 
head = wb.find( "wb:Header", ns ) 
consignee = head.find( "wb:Consignee", ns ) 
ul = consignee.find( "oref:UL", ns ) 
name = ul.find( "oref:ShortName", ns ) 

print( name.text )


# consignee = tree.findall( "wb:Consignee", ns ) 
# print( root ) # Documents
# print( consignee )
# print( root.nsmap )
# <ns:Document>
# print( doc ) # Document

# ООО "ТД Орловский каравай"