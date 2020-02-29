import sys
import os
from dir_creator import DirectoryCreator
def DisplayHelp():
	print("xml2dir allows to generate Folder structure as defined in the given Xml")
	print("xml2dir [h]	[g path]")
	print("h	Help")
	print("g	Generate")
	print("s	Display Sample Xml")
	print("path	Path to Xml File")
	exit(0)

def DisplaySampleXml():
	print("Sample File")
	print(".............")
	file = open("sample.xml")
	print(file.read())

if len(sys.argv) == 1:
	DisplayHelp()

if len(sys.argv) == 2:
	if(sys.argv[1]=="h"):
		DisplayHelp()
	elif(sys.argv[1]=="s"):
		DisplaySampleXml()
	else:
		DisplayHelp()


if sys.argv[1] == "g" and len(sys.argv)==3 :
	dirCreator = DirectoryCreator(sys.argv[2])
	dirCreator.ProcessXmlFile()

