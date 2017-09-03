#theme.py
from libs.config import app
from libs.classes import createFiles as createClass
from subprocess import call
import urllib.request
import os

def init():
	#define config vars
	ROOT_FOLDER = os.environ.get("ROOT_FOLDER")	
	PLUGINS_FOLDER = os.environ.get("PLUGINS_FOLDER")
	THEME_FOLDER = os.environ.get("THEME_FOLDER")
	VIEWS_FOLDER = os.environ.get("VIEWS_FOLDER")
	PARTIALS_FOLDER = os.environ.get("PARTIALS_FOLDER")
	ACF_KEY = os.environ.get("ACF_KEY")

	tmp = 'tmp/'

	files = createClass.createClass()
	files.dir_exist(tmp)

	# Composer install
	call('cd' + ROOT_FOLDER + '&& composer install', shell=True)

	# Fetch ACF (bought plugins) & move it to plugins
	if (ACF_KEY != 'INSERTKEY'):
		if files.file_exist(tmp + 'advanced-custom-fields-pro') == False and files.file_exist(str(PLUGINS_FOLDER) + 'advanced-custom-fields-pro') == False:
			filename = 'acf'
			response = urllib.request.urlretrieve('https://connect.advancedcustomfields.com/index.php?p=pro&a=download&k=' + str(ACF_KEY), tmp + filename + '.zip')
			call('unzip ' + tmp + filename + '.zip -d ' + tmp, shell=True)
			if files.file_exist(tmp + 'advanced-custom-fields-pro'):
				os.rename(tmp + 'advanced-custom-fields-pro', PLUGINS_FOLDER + 'advanced-custom-fields-pro')
				files.response(PLUGINS_FOLDER + 'advanced-custom-fields-pro')

	# Fetch starter theme GIT to tmp folder
	tmp_theme_name = 'starter-theme/'
	if files.file_exist(tmp + tmp_theme_name) == False:
		call('git clone https://github.com/timber/starter-theme.git ' + tmp + tmp_theme_name, shell=True)

	# Copy over only the data (functions.php, html_header, footer etc) we need
	root_files = ['header.php', 'footer.php', 'index.php', 'page.php', 'single.php', 'functions.php', 'screenshot.png']
	partials_files = ['html-header.twig', 'footer.twig']
	views_files = ['page.twig', 'single.twig']
	for file in root_files:
		if files.file_exist(tmp + tmp_theme_name + file):
			files.dir_exist(THEME_FOLDER)
			os.rename(tmp + tmp_theme_name + file, THEME_FOLDER + file)
			files.response(THEME_FOLDER + file)
	for file in partials_files:
		if files.file_exist(tmp + tmp_theme_name + 'templates/' + file):
				files.dir_exist(PARTIALS_FOLDER)
				os.rename(tmp + tmp_theme_name + 'templates/' + file, PARTIALS_FOLDER + file)
				files.response(PARTIALS_FOLDER + file)
	for file in views_files:
		if files.file_exist(tmp + tmp_theme_name + 'templates/' + file):
				files.dir_exist(VIEWS_FOLDER)
				os.rename(tmp + tmp_theme_name + 'templates/' + file, VIEWS_FOLDER + file)
				files.response(VIEWS_FOLDER + file)


	# Create custom style.css through input questions
	print('Creating style.css..')
	themename = input('Theme name for stylesheet? ')
	description = input('Theme description for stylesheet? ')

	if themename and description:
		files.createFile(
			'style.css',
			THEME_FOLDER,
			"/*\n" +
			"* Theme Name: " + themename + "\n" +
			"* Description: " + description + "\n" +
			"* Author: Wallop.ca" + "\n" +
			"*/"
		)