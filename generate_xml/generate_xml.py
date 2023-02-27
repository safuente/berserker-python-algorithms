import lxml.builder


def generate_xml(output_file):
    E = lxml.builder.ElementMaker()
    ROOT = E.root
    ITEM = E.item
    FIELD1 = E.field1
    FIELD2 = E.field2
    the_doc = ROOT(
            ITEM(
                FIELD1('test value 1', name='field-1'),
                FIELD2('test value 2', name='field-2'),
                )   
            )   
    f = open(output_file, "wb")
    f.write(lxml.etree.tostring(the_doc, pretty_print=True))
    f.close()
    

print('Example 1')
generate_xml('output.xml')
