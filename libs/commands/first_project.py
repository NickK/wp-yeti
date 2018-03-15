#theme.py
from libs.config import app
from libs.classes import createFiles as createClass
from subprocess import call
import urllib.request
import os
import shutil


class FirstProject:
	#define config vars	

	def __init__(self):
		#define config vars
		self.ACF_KEY = os.environ.get("ACF_KEY")
		self.ROOT_FOLDER = os.environ.get("ROOT_FOLDER")	
		self.PLUGINS_FOLDER = os.environ.get("PLUGINS_FOLDER")
		self.PARTIALS_FOLDER = os.environ.get("PARTIALS_FOLDER")
		self.TEMP_FOLDER = 'tmp/'
		self.THEME_FOLDER = os.environ.get("THEME_FOLDER")
		self.VIEWS_FOLDER = os.environ.get("VIEWS_FOLDER")

		self.fetchCoreAndPlugins()
		self.fetchStarterTheme()
		self.createThemeFiles()
		self.cleanFiles()

	def fetchCoreAndPlugins(self):

		files = createClass.createClass()
		files.dir_exist(self.TEMP_FOLDER)

		# Composer install
		call('cd ' + self.ROOT_FOLDER + '&& composer install', shell=True)

		# Fetch ACF (bought plugins) & move it to plugins
		if (self.ACF_KEY != 'INSERTKEY'):
			if files.file_exist(str(self.PLUGINS_FOLDER) + 'advanced-custom-fields-pro') == False:
				filename = 'acf'
				response = urllib.request.urlretrieve('https://connect.advancedcustomfields.com/index.php?p=pro&a=download&k=' + str(self.ACF_KEY), self.TEMP_FOLDER + filename + '.zip')
				
				print(files.file_exist(self.TEMP_FOLDER + 'advanced-custom-fields-pro'))

				if files.file_exist(self.TEMP_FOLDER + 'advanced-custom-fields-pro') == False:
					call('unzip ' + self.TEMP_FOLDER + filename + '.zip -d ' + self.TEMP_FOLDER, shell=True)
				
				if files.file_exist(self.TEMP_FOLDER + 'advanced-custom-fields-pro'):
					os.rename(self.TEMP_FOLDER + 'advanced-custom-fields-pro', self.PLUGINS_FOLDER + 'advanced-custom-fields-pro')
					files.response(self.PLUGINS_FOLDER + 'advanced-custom-fields-pro')

	def fetchStarterTheme(self):
		files = createClass.createClass()

		# Fetch starter theme GIT to tmp folder
		tmp_theme_name = 'starter-theme/'
		if files.file_exist(self.TEMP_FOLDER + tmp_theme_name) == False:
			call('git clone https://github.com/timber/starter-theme.git ' + self.TEMP_FOLDER + tmp_theme_name, shell=True)


		# Copy over only the data (functions.php, html_header, footer etc) we need
		root_files = ['header.php', 'footer.php', 'page.php', 'functions.php', 'screenshot.png', '404.php']
		partials_files = ['html-header.twig', 'footer.twig']
		views_files = ['page.twig', '404.twig']

		blogs = input('Add blog files? (y/n) ')
		if (blogs == 'y'):
			root_files.extend(['index.php', 'archive.php', 'search.php', 'single.php'])
			views_files.extend(['index.twig', 'single.twig'])

		author = input('Add author file? (y/n) ')
		if (author == 'y'):
			root_files.extend(['author.php'])
			views_files.extend(['author.twig'])



		for file in root_files:
			if files.file_exist(self.TEMP_FOLDER + tmp_theme_name + file):
				files.dir_exist(self.THEME_FOLDER)
				shutil.copyfile(self.TEMP_FOLDER + tmp_theme_name + file, self.THEME_FOLDER + file)
				files.response(self.THEME_FOLDER + file)
		for file in partials_files:
			if files.file_exist(self.TEMP_FOLDER + tmp_theme_name + 'templates/' + file):
					files.dir_exist(self.PARTIALS_FOLDER)
					shutil.copyfile(self.TEMP_FOLDER + tmp_theme_name + 'templates/' + file, self.PARTIALS_FOLDER + file)
					files.response(self.PARTIALS_FOLDER + file)
		for file in views_files:
			if files.file_exist(self.TEMP_FOLDER + tmp_theme_name + 'templates/' + file):
					files.dir_exist(self.VIEWS_FOLDER)
					shutil.copyfile(self.TEMP_FOLDER + tmp_theme_name + 'templates/' + file, self.VIEWS_FOLDER + file)
					files.response(self.VIEWS_FOLDER + file)


	def createThemeFiles(self):
		files = createClass.createClass()

		# Create custom style.css through input questions
		print('Creating style.css..')
		themename = input('Theme name for stylesheet? ')
		description = input('Theme description for stylesheet? ')

		if themename and description:
			files.createFile(
				'style.css',
				self.THEME_FOLDER,
				"/*\n" +
				"* Theme Name: " + themename + "\n" +
				"* Description: " + description + "\n" +
				"* Author: Wallop.ca" + "\n" +
				"*/"
			)


	def cleanFiles(self):
		#remove tmp folder
		print('Clean up files..')
		call('rm -rf ' + self.TEMP_FOLDER, shell=True)