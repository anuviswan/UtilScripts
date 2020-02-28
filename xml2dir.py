from eyed3 import id3
import os
import sys
import shutil
import re

def DisplayHelp():
	print("xml2dir allows to generate Folder structure as defined in the given Xml")
	print("xml2dir [h]	[g path]")
	print("h	Help")
	print("g	Generate")
	print("path	Path to Xml File")
	exit(0)


if len(sys.argv) == 1:
	DisplayHelp()

print(sys.argv)

