# Intends to sort and group Mp3 files in given folder to nested folders.
from eyed3 import id3
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


def Sort_Mp3(filePath):
	result = GetAlbumName(filePath)
	print(result)

Sort_Mp3(arg)
