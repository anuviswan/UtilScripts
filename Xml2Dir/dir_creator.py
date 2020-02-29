import sys
import os

class DirectoryCreator:
	def __init__(self,filePath):
		self.FilePath = filePath

	def ValidateFilePath(self,filePath):
		return bool(os.path.exists(filePath))

	def ProcessXmlFile(self):
		if(not self.ValidateFilePath(self.FilePath)):
			print("Invalid File Path")
			exit(0)
		
		print("Processing File"+self.FilePath)


