#theme.py
from libs.config import app
from libs.classes import createFiles as createClass
from subprocess import call
import urllib.request
import os
import shutil
import fileinput

class BuildProject:
	#define config vars	

	def __init__(self):
		self.ACF_KEY = os.environ.get("ACF_KEY")
		self.FILES_FOLDER = os.environ.get('FILES_FOLDER')
		self.PARTIALS_FOLDER = os.environ.get("PARTIALS_FOLDER")
		self.PLUGINS_FOLDER = os.environ.get("PLUGINS_FOLDER")
		self.ROOT_FOLDER = os.environ.get("ROOT_FOLDER")	
		self.THEME_FOLDER = os.environ.get("THEME_FOLDER")
		self.VIEWS_FOLDER = os.environ.get("VIEWS_FOLDER")

		self.DB_USER = os.environ.get("DB_USER")
		self.DB_PASSWORD = os.environ.get("DB_PASSWORD")
		self.DB_NAME = os.environ.get("DB_NAME")

		self.fetchFiles()
		self.handleDB()


	def fetchFiles(self):
		tmp = 'tmp/'

		files = createClass.createClass()
		files.dir_exist(tmp)

		core = input('Setup & download WordPress + Plugins? (y/n): ')
		multisite = input('Multi-site installation? (y/n): ')
		if core == 'y':
			# Composer install
			call('cd ' + self.ROOT_FOLDER + '&& composer install', shell=True)

			# Fetch ACF (bought plugins) & move it to plugins
			if (self.ACF_KEY != 'INSERTKEY'):
				if files.file_exist(str(self.PLUGINS_FOLDER) + 'advanced-custom-fields-pro') == False:
					filename = 'acf'
					response = urllib.request.urlretrieve('https://connect.advancedcustomfields.com/index.php?p=pro&a=download&k=' + str(self.ACF_KEY), tmp + filename + '.zip')
					
					print(files.file_exist(tmp + 'advanced-custom-fields-pro'))

					if files.file_exist(tmp + 'advanced-custom-fields-pro') == False:
						call('unzip ' + tmp + filename + '.zip -d ' + tmp, shell=True)
					
					if files.file_exist(tmp + 'advanced-custom-fields-pro'):
						os.rename(tmp + 'advanced-custom-fields-pro', self.PLUGINS_FOLDER + 'advanced-custom-fields-pro')
						files.response(self.PLUGINS_FOLDER + 'advanced-custom-fields-pro')


			# Custom wp-config file
			if multisite:
				shutil.copy(self.FILES_FOLDER + 'multisite-config.php', self.ROOT_FOLDER + 'wp-config.php')
			else:
				shutil.copy(self.FILES_FOLDER + 'regular-config.php', ROOT_FOLDER + 'wp-config.php')

			#remove tmp folder
			call('rm -rf tmp', shell=True)

	def handleDB(self):
			database = input('Setup database? (y/n): ')
			if database == 'y':
				print('This script will search and replace and import the database for you..')
				dbpath = input('Where on your computer is the database located? Feed me absolute path + file name: ')
				search = input('Search for (case sensitive string): ')
				replace = input('Replace with: ')
				pointofnoreturn = input('WARNING! Make sure your DB is set correctly inside your .env file. Proceed? (y/n): ')
				if pointofnoreturn:

					with fileinput.FileInput(dbpath, inplace=True, backup='.bak') as file:
					    for line in file:
					        print(line.replace(search, replace), end='')

					call('mysql -u '+ self.DB_USER +' -p' + self.DB_PASSWORD + ' ' + self.DB_NAME + ' < "' + dbpath + '"', shell=True)