#acf.py
from libs.config import app
from libs.classes import createFiles as createClass
import urllib.request
import os

def global_general():

	#define config vars
	ACF_JSON_FOLDER = os.environ.get("ACF_JSON_FOLDER")

	# define filename
	filename = 'group_5924c60418aa5'
	#get file from site
	response = urllib.request.urlretrieve(app.config['production'] + 'acf/' + filename + '.json', filename + '.json')
	
	files = createClass.createClass()
	files.dir_exist(ACF_JSON_FOLDER)
	if files.file_exist(ACF_JSON_FOLDER + filename + '.json') == False:
		#move downloaded file to correct server
		os.rename(filename + '.json', ACF_JSON_FOLDER + filename + '.json')
		files.response(ACF_JSON_FOLDER + filename + '.json')

def maps():

	#define config vars
	ACF_JSON_FOLDER = os.environ.get("ACF_JSON_FOLDER")

	files_list = ['group_58e2e23fe9d48', 'group_58e3d20cb88e9']
	for file in files_list:
		filename = file
		response = urllib.request.urlretrieve(app.config['production'] + 'acf/' + filename + '.json', filename + '.json')
	
		files = createClass.createClass()
		files.dir_exist(ACF_JSON_FOLDER)
		if files.file_exist(ACF_JSON_FOLDER + filename + '.json') == False:
			os.rename(filename + '.json', ACF_JSON_FOLDER + filename + '.json')
			files.response(ACF_JSON_FOLDER + filename + '.json')


def gallery():
	#define config vars
	ACF_JSON_FOLDER = os.environ.get("ACF_JSON_FOLDER")
	
	#define filename
	filename = 'group_594158f5097e7'
	#get file from site
	response = urllib.request.urlretrieve(app.config['production'] + 'acf/' + filename + '.json', filename + '.json')

	files = createClass.createClass()
	files.dir_exist(ACF_JSON_FOLDER)
	if files.file_exist(ACF_JSON_FOLDER + filename + '.json') == False:
		os.rename(filename + '.json', ACF_JSON_FOLDER + filename + '.json')
		files.response(ACF_JSON_FOLDER + filename + '.json')