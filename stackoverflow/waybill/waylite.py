from lxml import etree
import sqlite3
tree = etree.parse( "WayBill.xml" )
root = tree.getroot() # Documents
ns = root.nsmap
consignee = root.find( './/wb:Consignee', ns ) 
name = consignee.find( ".//oref:ShortName", ns )
inn  = consignee.find( ".//oref:INN"      , ns )
kpp  = consignee.find( ".//oref:KPP"      , ns )

try :
  con = sqlite3.connect( 'Clurichaun.sqlite' ) 
  cursor = con.cursor()
  cursor.execute( "insert into dict_Organization( IsLegalEntity, Name, INN, KPP ) values ( 1, '" + name.text + "', " + inn.text + ", " + kpp.text + " ) " )
  con.commit()
finally :
  con.close()





