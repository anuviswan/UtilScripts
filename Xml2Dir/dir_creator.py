import sys
import os
import xml.etree.ElementTree as ET 

class DirectoryCreator:
	def __init__(self,filePath):
		self.FilePath = filePath.lower()

	def ValidateFilePath(self,filePath):
		return bool(os.path.exists(filePath)) 

	def ReadXmlFile(self,filePath):
		tree = ET.parse(filePath)
		root = tree.getroot()
		rootDir = root.attrib["rootPath"]
		rootDirName = root.attrib["name"]
		rootDirPath = os.path.join(rootDir,rootDirName)
		self.GenerateDirectory(rootDirPath)
		self.ReadXmlNode(root,rootDirPath)

	def ReadXmlNode(self,node,currentPath):
		for element in node.getchildren():
			name = element.attrib["name"]
			path = os.path.join(currentPath,name)
			print(element.tag.title())
			if(element.tag == "file"):
				self.GenerateFile(path)
			else:
				self.GenerateDirectory(path)
				self.ReadXmlNode(element,path)
			
	def GenerateDirectory(self,path):
		if not os.path.isdir(path):
			os.mkdir(path)

	def GenerateFile(self,path):
		if not os.path.isfile(path):
			with open(path,'w') as file:
				pass

	@property
	def IsSupportedFileType(self):
		return (os.path.splitext(self.FilePath)[1] == ".xml")
		

	def ProcessXmlFile(self):
		print("Processing File: " + self.FilePath + "....")

		if(not self.ValidateFilePath(self.FilePath)):
			print("Invalid File Path")
			exit(0)

		if(not self.IsSupportedFileType):
			print("Unsupported File Type")
			exit(0)
		
		print("Validated File Path....")
		self.ReadXmlFile(self.FilePath)
		



