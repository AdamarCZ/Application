import xml.etree.ElementTree as ET
import shutil

try:
    #parsing xml
    tree = ET.parse("config.xml")
    root = tree.getroot()

    #files operations
    files = root.findall("file")
    for part in files:
        fileName = part.get("file_name")
        sourcePath = part.get("source_path") + "/" + fileName
        destinationPath = part.get("destination_path") + "/" + fileName
        

        try:
            shutil.copy2(sourcePath, destinationPath)
        except:
            print("File {} not found or access denied!".format(fileName))

except:
    print("Config file must be in same directory!")





