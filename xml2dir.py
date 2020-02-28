import sys

def DisplayHelp():
	print("xml2dir allows to generate Folder structure as defined in the given Xml")
	print("xml2dir [h]	[g path]")
	print("h	Help")
	print("g	Generate")
	print("path	Path to Xml File")
	exit(0)


if len(sys.argv) == 1:
	DisplayHelp()

if sys.argv[1] == "g" and len(sys.argv)==3 :
	print("filePath : " + sys.argv[2])

print(sys.argv)
