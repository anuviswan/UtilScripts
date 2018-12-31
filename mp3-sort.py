# Intends to sort and group Mp3 files in given folder to nested folders.
from eyed3 import id3
import os
import sys

arg = sys.argv[1]

# Get Album/Artist Name for given mp3
def GetAlbumName(filename):
	tag = id3.Tag()
	tag.parse(filename)
	albumName = tag._getAlbum()
	artistName = tag._getArtist()
	
	if(albumName=="None"):
		if(artistName=="None"):
			return "Unsorted"
		else:
			return artistName
	else:
		return albumName

def GetAllFilesFromFolder(folderPath,extension):
	return (os.path.join(folderPath,file) for file in os.listdir(folderPath) if file.endswith('.' + extension))

def Sort_Mp3(folderPath):
	files = GetAllFilesFromFolder(folderPath,"mp3")
	for file in files:
		print(GetAlbumName(file))
	

Sort_Mp3(arg)
