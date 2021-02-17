import os

path = '/home/yicheng01/darknet/VOCdevkit/VOC2012/JPEGImages'

for file in os.listdir(path):
	if "IMG" in file:
		print(path + "/" + file)
