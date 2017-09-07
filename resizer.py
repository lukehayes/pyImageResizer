#!/usr/bin/env python

from PIL import Image
import glob, os, sys, getopt

currentDir = os.getcwd()
width = sys.argv[1]
outputDir = sys.argv[2] + "/"

os.mkdir(outputDir)

for i in glob.glob("*.jpg"):
	img = Image.open(i)
	height = width * img.size[1] / img.size[0]
	name = os.path.splitext(i)[0]
	fileType = os.path.splitext(i)[1]
	rsz = img.resize((width,height))
	rsz.save(outputDir + name + fileType)