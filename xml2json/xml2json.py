import json
import xmltodict

with open('./xml2json/input.xml') as xml_file: 
    # Parse xml file to a dict type
    data_parsed = xmltodict.parse(xml_file.read())

    xml_file.close()

    # Serializing to json 
    json_form = json.dumps(data_parsed)

    with open('./xml2json/output.json', 'w') as json_file:
        json_file.write(json_form)

        json_file.close()


