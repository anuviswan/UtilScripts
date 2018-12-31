# Intends to sort and group Mp3 files in given folder to nested folders.
from eyed3 import id3
import os
import sys
import shutil
import re

# read command line arg : Folder Name
arg = sys.argv[1]

# Get Album/Artist Name for given mp3
def GetAlbumName(filename):
	tag = id3.Tag()
	tag.parse(filename)
	albumName = tag._getAlbum()
	artistName = tag._getArtist()
	print(albumName)
	if(albumName==None):
		if(artistName==None):
			return "Unsorted"
		else:
			return artistName
	else:
		return albumName

# Return all files in the folder that has the specified extension
def GetAllFilesFromFolder(folderPath,extension):
	return (os.path.join(folderPath,file.lower()) for file in os.listdir(folderPath) if file.lower().endswith('.' + extension))

# Sort files into Album/Artist Names
def Sort_Mp3(folderPath):
	files = GetAllFilesFromFolder(folderPath,"mp3")
	for file in files:
		albumName = GetAlbumName(file)
		foldername = "Unsorted"
		re2 =  re.compile(r"^[^<>/{}[\]~`\.]*$");
		if re2.match(albumName):
			print("Found match %s" %albumName)
			foldername = albumName
		albumFolder = os.path.join(folderPath, foldername)
		if not os.path.exists(albumFolder):
			os.makedirs(albumFolder)
		
		fileName = os.path.basename(file)
		shutil.move(file,os.path.join(albumFolder,fileName))
		print(os.path.join(albumFolder,fileName))
	

Sort_Mp3(arg)
