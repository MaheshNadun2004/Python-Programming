import xml.etree.ElementTree as ET

xml_data = """<motorvehicles>
<vehicle>
<registration_no>CBB1456</registration_no>
<make>Toyota</make>
<model>Premio</model>
</vehicle>
<vehicle>
<registration_no>PR2245</registration_no>
<make>Mazda</make>
<model>Bongo</model>
</vehicle>
<vehicle>
<registration_no>DE2115</registration_no>
<make>TATA</make>
<model>Sumo</model>
</vehicle>
<vehicle>
<registration_no>CAR7785</registration_no>
<make>Kia</make>
<model>Optima</model>
</vehicle>
</motorvehicles>"""

root = ET.fromstring(xml_data)

for vehicle in root.findall('vehicle'):
    reg_no = vehicle.find('registration_no').text
    if reg_no == 'DE2115':
        vehicle.find('make').text = 'Nissan'
        vehicle.find('model').text = 'Skyline'


for vehicle in root.findall('vehicle'):
    make = vehicle.find('make').text
    if make == 'Nissan':
        print(vehicle.find('registration_no').text)
