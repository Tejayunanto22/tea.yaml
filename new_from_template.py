#!/usr/bin/env python3
import sys
import os
import subprocess
import datetime
from pathlib import Path
import create_make
from subprocess import PIPE, Popen
def help_msg(file_types):
	print("NFT e.g. New From Template \n   A helper script to quickly create files from a standard template. \n   Takes any file with one of the following extentions:")
	for k, v in list(file_types.items()):
		print("\t{:<20}{:<20}".format("<filename>.{}".format(k), "creates a {} file".format(v)))
		
	exit()

def edit_template(TEMPLATE_STR, FILE_PREFIX, PROJECT):

	now = datetime.datetime.now()
	date = ("{}-{}-{}".format(now.month, now.day, now.year))

	TEMPLATE_STR = TEMPLATE_STR.replace("<date>", date)
	TEMPLATE_STR = TEMPLATE_STR.replace("<filename>", FILE_PREFIX)
	TEMPLATE_STR = TEMPLATE_STR.replace("<project>", PROJECT)
	return TEMPLATE_STR


path = os.getcwd()
template_dir = os.path.dirname(os.path.abspath(__file__)) + '/templates'
project = path.split("/")[-1]
file_types = {"py":"python", "c":"C", "java":"Java", "csh":"csh", "sh":"bash" }
other_files = {"README":"README" , "Makefile" : "Makefile"}

new_file = sys.argv[-1]
ext = new_file.split(".")[-1]
prefix = new_file.split(".")[0]

if('-h' in sys.argv[-1] or len(sys.argv) <= 1 ):
	help_msg(file_types)

if(ext in file_types):
	template_name= template_dir+ "/"+file_types[ext]+ '.' + ext
elif(new_file == "README"):
	template_name = template_dir+ "/README"
elif(new_file == "Makefile"):
	create_make.consruct(path, template_dir)
	exit()
else:
	print ("Oops, invalid input \'{}\'. \nTry one of the following:".format(new_file))
	for k in list(file_types.keys()):
		print("\t<filename>.{}".format(k))
	exit()

template_file = open(template_name, 'r')
template = template_file.read()

template = edit_template(template, prefix, project)
output_file = open("./"+new_file, 'w')
output_file.write(template)
output_file.close()




