import xml.etree.ElementTree as ET
from PyPDF2 import PdfFileReader, PdfFileWriter

sourcePath = ""
Parts = []

xmlSource = ET.parse("Source.xml")
root = xmlSource.getroot()

files = root.findall("file")

if(len(files) > 0):
    sourcePath = files[0].get("path")

for part in root.findall("parts/part"):
    name = part.get("name")
    start = part.get("start")
    end = part.get("end")
    Parts.append([name,start,end])

if not sourcePath:
    print("source file is missing.")    
else:    
    reader = PdfFileReader(open(sourcePath,"rb"))
    
    for part in Parts:
        writer = PdfFileWriter()
        for i in range(int(part[1]), int(part[2]) +1):
            writer.addPage(reader.getPage(i))
        
        with open(part[0]+".pdf","wb") as outputStream:
            writer.write(outputStream)


        

