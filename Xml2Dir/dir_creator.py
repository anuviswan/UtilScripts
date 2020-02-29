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
			dirName = element.attrib["name"]
			dirPath = os.path.join(currentPath,dirName)
			print(dirPath)
			self.GenerateDirectory(dirPath)
			self.ReadXmlNode(element,dirPath)
			
	def GenerateDirectory(self,path):
		os.mkdir(path)


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
		



