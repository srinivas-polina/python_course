import xml.etree.ElementTree as ET #this module is allows us to manipulate XML files.

def parse_xml_et(fn): #fn is the name of the file we want to parse.
    tree = ET.parse(fn) #this function parse the XML file and returns an ElementTree Object.
    root = tree.getroot() #getting main node of the XML file by invoking the getroot() method from tree.
    #now we have the XML's main node or root, we can print the root's name attributes as follows:
    print("Domains for: ", root.attrib["name"])
    #now we want to be able toprint each of the domains and we can do that by iterating over each child found within the root of the XML file.
    for child in root:
        print("\t", child.attrib["name"], child.tag) #we can print the value of the name attribute and also the value of a child tag

#we can invoke the parse_xml_et function and pass the name of the XML file we want to parse as an argument:
parse_xml_et("./files_to_read/ef_author.xml")

#creating a function to add an xml element to an XML file.
#to which we can pass the name of the XML file tha we want to write to, the element or node we want to add, the node attribute and the value that we want to write.
def add_xml_element_et(fn, el, attr, val):
    #then we need to invoke the parse method from ET, passing the name of the xml file that we want to write to
    tree = ET.parse(fn)
    #after that, we can get the main node of the XML file by invoking the getroot method from tree, which was returned by the parse method.
    root = tree.getroot()
    #now we have the main node of the XML file, we can create the child element from the root by invoking the element method from ET and passing the name of the element or node we want to access.
    child = ET.Element(el)
    #once we have created the child element, we can access the nodes attributes and assign it to the value that we want to add.
    child.attrib[attr] = val
    #then all we need to do is to invoke the append method of root and pass the child node as an argument we created, which will add the child node to the XML file.
    root.append(child)
    #finally we ca write the XML by calling the write method from tree and passing the name of the resultant xml file as an argument.
    tree.write(fn)
    
#calling the add_xml_element_et function and passing the name of the XML file we want to write to, the name of the child node we want to add, the name of the child node attribute and the value of the child node attributethat we want to write as argument:
add_xml_element_et("./files_to_read/ef_author.xml","domain", "name", "Java")
#after running this code, we can see that a new node was added with the attribute and value specified.
#like: <domain name = "Java"/></author>

#the original XML file looked like this:
#<author name = "John Doe">
#    <domain name = "Python"/>
#    <domain name = "Azure"/>
#    <domain name = "Aws"/>
#<domain name = "Java"/></author>


#creating a function tha will allow us to change the value of an existing child or node.
#we need to pass the name of the XML file to modify, th ename of the element or node we want to modify, the name of the attribute we want to modify and the old and new value that we want to assign to that attribute.
def change_xml_element_et(fn, el, attr, oldval, newval):
    #frist we need to get access to XML structure, and we can do that by invoking the parse method from ET, parsing the name of the XML file
    tree = ET.parse(fn)
    #then we can get the main node by calling the getroot method from tree.
    root = tree.getroot()
    #and then we need to locate the node we want to update, which we can do by invoking the find method from the XML's root, we can find the node that we want to modify by passing the name of the element, then indicating the attributes name, and then the nodes old value that we want to change.
    child = root.find("./" + el + "[@" + attr + "='" + oldval + "']")
    #once the node is found, we ca change the attribute value by assigning the new value.
    child.attrib[attr] = newval
    #then we can commit the changes by invoking the write method from tree and passing the name of the XML file
    tree.write(fn)

#lets invoke the change_xmL_element_et function by passing the name of the XML file we want to modify, the name of the node we wnat to modify, the name of the node attribute we want to modify, the old value we want to change and the new value we want to assign to that attributes as an argument.
change_xml_element_et("./files_to_read/ef_author", "domain", "name", "Java", "JavaScript" )

