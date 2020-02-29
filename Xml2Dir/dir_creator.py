import sys
import os

class DirectoryCreator:
	def __init__(self,filePath):
		self.FilePath = filePath

	def ValidateFilePath(self,filePath):
		return bool(os.path.exists(filePath))

	def ProcessXmlFile(self):
		print("Processing File: " + self.FilePath + "....")

		if(not self.ValidateFilePath(self.FilePath)):
			print("Invalid File Path")
			exit(0)
		
		print("Validated File Path....")
		



