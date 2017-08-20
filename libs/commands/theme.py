#template.py
from libs.config import app
from libs.classes import createFiles as createClass
from subprocess import call
import urllib.request
import os

def init():
	tmp = 'tmp/'
	files = createClass.createClass()
	files.dir_exist(tmp)

	# Composer install
	root_directory = ' ../../../../ '
	call('cd' + root_directory + '&& composer install', shell=True)

	# Fetch ACF + ninjaforms (bought plugins) & move it to plugins
	if files.file_exist(tmp + 'advanced-custom-fields-pro') == False and files.file_exist(app.config['folders']['plugins'] + 'advanced-custom-fields-pro') == False:
		filename = 'acf'
		response = urllib.request.urlretrieve('https://connect.advancedcustomfields.com/index.php?p=pro&a=download&k=' + app.config['acf']['key'], tmp + filename + '.zip')
		call('unzip ' + tmp + filename + '.zip -d ' + tmp, shell=True)
		if files.file_exist(tmp + 'advanced-custom-fields-pro'):
			os.rename(tmp + 'advanced-custom-fields-pro', app.config['folders']['plugins'] + 'advanced-custom-fields-pro')
			files.response(app.config['folders']['plugins'] + 'advanced-custom-fields-pro')

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
			files.dir_exist(app.config['folders']['theme_folder'])
			os.rename(tmp + tmp_theme_name + file, app.config['folders']['theme_folder'] + file)
			files.response(app.config['folders']['theme_folder'] + file)
	for file in partials_files:
		if files.file_exist(tmp + tmp_theme_name + 'templates/' + file):
				files.dir_exist(app.config['folders']['partials'])
				os.rename(tmp + tmp_theme_name + 'templates/' + file, app.config['folders']['partials'] + file)
				files.response(app.config['folders']['partials'] + file)
	for file in views_files:
		if files.file_exist(tmp + tmp_theme_name + 'templates/' + file):
				files.dir_exist(app.config['folders']['views'])
				os.rename(tmp + tmp_theme_name + 'templates/' + file, app.config['folders']['views'] + file)
				files.response(app.config['folders']['views'] + file)


	# Create custom style.css through input questions
	print('Setting up style.css..')
	themename = input('Theme Name? ')
	description = input('Theme Description? ')

	if themename and description:
		files.createFile(
			'style.css',
			app.config['folders']['theme_folder'],
			"/*\n" +
			"* Theme Name: " + themename + "\n" +
			"* Description: " + description + "\n" +
			"* Author: Wallop.ca" + "\n" +
			"*/"
		)