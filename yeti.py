import os
import argparse
from libs.commands import *
from libs.config import app
from dotenv import load_dotenv

#load env file
dotenv_path = '../.env'
load_dotenv(dotenv_path)


class Yeti:
	def __init__(self):

		parser = argparse.ArgumentParser(prog='WP Yeti')
		parser.add_argument('-v', '--version', dest='version', action='store_true', help='Get version number of WP-Yeti')

		# Create files inside theme folder
		parser.add_argument('--make:template', dest='make_template', metavar='name', help='Create a page template file')
		parser.add_argument('--make:page', dest='make_page', metavar='name', help='Create a page file')
		parser.add_argument('--make:single', dest='make_single', metavar='name', help='Create a single page file')
		parser.add_argument('--make:taxonomy', dest='make_taxonomy', metavar='name', help='Create a new taxonomy file')
		parser.add_argument('--make:custom_posts', dest='make_customposts', metavar='name', help='Create a new custom post file')
		parser.add_argument('--make:js', dest='make_js', metavar='name', help='Create a new JS file')
		parser.add_argument('--make:ajax', dest='make_ajax', metavar='functionname', help='Create a new AJAX file')
		parser.add_argument('--make:api', dest='make_api', metavar='functionname', help='Create a new API file')		

		# Download and add ACF files
		parser.add_argument('--make:acf_global_general', dest='make_acf_global_general', action='store_true', help='Create ACF file for general (social media, error)')		
		parser.add_argument('--make:acf_gallery', dest='make_acf_gallery', action='store_true', help='Create ACF file for Gallery')		
		parser.add_argument('--make:acf_maps', dest='make_acf_maps', action='store_true', help='Create ACF files for Maps')		

		# Build files
		parser.add_argument('--build:first_project', dest='first_project', action='store_true', help='Build theme (Starter Theme etc)')
		parser.add_argument('--build:finished_project', dest='finished_project', action='store_true', help='Help setup project')
		parser.add_argument('--build:configure_db', dest='configure_db', action='store_true', help='Default configuration for database')

		# Insert scripts to functions.php
		parser.add_argument('--insert:scripts', dest='insert_scripts', action='store_true', help='Add wp_enqueue_scripts to functions file')
		parser.add_argument('--insert:api_routing', dest='insert_api_routing', action='store_true', help='Add Routes::map to functions file')
		parser.add_argument('--insert:options_menu', dest='insert_options_menu', action='store_true', help='Add register_options_page to functions file')
		parser.add_argument('--insert:images', dest='insert_images', action='store_true', help='Add add_image_size to functions file')
		parser.add_argument('--insert:menus', dest='insert_menus', action='store_true', help='Add menus to functions file')		
		parser.add_argument('--insert:cache_json', dest='insert_cache_json', action='store_true', help='Add cacheJSON class to functions file')		
		parser.add_argument('--insert:acf_gmaps_key', dest='insert_acf_gmaps_key', action='store_true', help='Add acf_update_setting (gmaps key) to functions file')
		parser.add_argument('--insert:acf_save_json', dest='insert_acf_save_json', action='store_true', help='Add ACF save/load JSON to functions file')


		args = parser.parse_args()
		self.getCommand(args)

	def getCommand(self, args):
		if args.version:
			print('Version: ' + str(app.config['version']))
		if args.make_template:
			template.Template(args.make_template)
			#template.init(args.make_template)
		if args.make_page:
			page.init(args.make_page)
		if args.make_single:
			single.init(args.make_single)
		if args.make_taxonomy:
			taxonomy.init(args.make_taxonomy)
		if args.make_customposts:
			custom_posts.init(args.make_customposts)
		if args.make_js:
			js.init(args.make_js)
		if args.make_ajax:
			ajax.init(args.make_ajax)
		if args.make_api:
			api.init(args.make_api)
		if args.make_acf_global_general:
			acf.global_general()
		if args.make_acf_gallery:
			acf.gallery()
		if args.make_acf_maps:
			acf.maps()
		if args.first_project:
			first_project.FirstProject()
		if args.finished_project:
			finished_project.BuildProject()
		if args.configure_db:
			db.configure_db()
		if args.insert_scripts:
			insert.Insert().scripts()
		if args.insert_api_routing:
			insert.Insert().api_routing()
		if args.insert_options_menu:
			insert.Insert().options()
		if args.insert_images:
			insert.Insert().images()
		if args.insert_menus:
			insert.Insert().menus()
		if args.insert_cache_json:
			insert.Insert().cache_json()

		if args.insert_acf_gmaps_key:
			insert.Insert().acf_gmaps_key()
		if args.insert_acf_save_json:
			insert.Insert().acf_save_json()


yeti = Yeti()