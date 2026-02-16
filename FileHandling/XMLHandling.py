import xml.etree.ElementTree as ET
tree=ET.parse("C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//Dataformats//employee.xml")
root=tree.getroot() #get the root element
print(root.tag)

#get the first child node/ tag
print(root[0].tag)
print(root[1].tag)

#get the attribute of the child node
print(root[0].attrib)
print(root[1].attrib)

#fetch all the attributes in the child node
##for employee in root.findall("employee"):
    ##emp_id=employee.get("id")
    ##print(emp_id)
    ##emp_id=employee.get("name")
    ##print(emp_id)
##for emp in root.findall("employee"):
    ##name= emp.get("name").text
    ##role = emp.get("role").text
    ##exp = emp.get("exp").text
    ##print(name.role.exp)

#root> child note>
#create the rooot element
root= ET.Element("employees")
#create= the child elements
emp1 = ET.SubElement(root,"employee",id="101")
ET.SubElement(emp1,"name").text="Amit"
ET.SubElement(emp1,"role").text="engineer"
ET.SubElement(emp1,"experience").text="4"



emp1 = ET.SubElement(root,"employee",id="102")
ET.SubElement(emp1,"name").text="Angel"
ET.SubElement(emp1,"role").text="engineer"
ET.SubElement(emp1,"experience").text="9"

#write to the file
tree= ET.ElementTree(root)
tree.write("C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//Dataformats//update.xml", encoding="utf-8", xml_declaration=True)

#updating the xml
tree=ET.parse("C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//Dataformats//update.xml")
root=tree.getroot()
for emp in root.findall("employee"):
    if emp.get("id")== "101" :
        emp.find("experience").text="16"
tree.write("C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//Dataformats//update.xml",encoding="utf-8", xml_declaration=True)














