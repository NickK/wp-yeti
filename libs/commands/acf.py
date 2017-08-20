#template.py
from libs.config import app
from libs.classes import createFiles as createClass
import urllib.request
import os

def global_general():
	# define filename
	filename = 'group_5924c60418aa5'
	#get file from site
	response = urllib.request.urlretrieve(app.config['production'] + 'acf/' + filename + '.json', filename + '.json')
	
	files = createClass.createClass()
	files.dir_exist(app.config['folders']['acf-json'])
	if files.file_exist(app.config['folders']['acf-json'] + filename + '.json') == False:
		#move downloaded file to correct server
		os.rename(filename + '.json', app.config['folders']['acf-json'] + filename + '.json')
		files.response(app.config['folders']['acf-json'] + filename + '.json')

def maps():
	files_list = ['group_58e2e23fe9d48', 'group_58e3d20cb88e9']
	for file in files_list:
		filename = file
		response = urllib.request.urlretrieve(app.config['production'] + 'acf/' + filename + '.json', filename + '.json')
	
		files = createClass.createClass()
		files.dir_exist(app.config['folders']['acf-json'])
		if files.file_exist(app.config['folders']['acf-json'] + filename + '.json') == False:
			os.rename(filename + '.json', app.config['folders']['acf-json'] + filename + '.json')
			files.response(app.config['folders']['acf-json'] + filename + '.json')


def gallery():
	#define filename
	filename = 'group_594158f5097e7'
	#get file from site
	response = urllib.request.urlretrieve(app.config['production'] + 'acf/' + filename + '.json', filename + '.json')

	files = createClass.createClass()
	files.dir_exist(app.config['folders']['acf-json'])
	if files.file_exist(app.config['folders']['acf-json'] + filename + '.json') == False:
		os.rename(filename + '.json', app.config['folders']['acf-json'] + filename + '.json')
		files.response(app.config['folders']['acf-json'] + filename + '.json')