import sys
import os

class DirectoryCreator:
	def __init__(self,filePath):
		self.FilePath = filePath.lower()

	def ValidateFilePath(self,filePath):
		return bool(os.path.exists(filePath)) 

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
		



