import os
import argparse
from libs.commands import *
from libs.config import app
from dotenv import load_dotenv

dotenv_path = '../.env'
load_dotenv(dotenv_path)


class Kleinisan:
	def __init__(self):

		parser = argparse.ArgumentParser(prog='Kleinisan')
		parser.add_argument('-v', '--version', dest='version', action='store_true', help='Get version number of kleinisan')

		parser.add_argument('--make:template', dest='make_template', metavar='name', help='Create a page template file')
		parser.add_argument('--make:page', dest='make_page', metavar='name', help='Create a page file')
		parser.add_argument('--make:single', dest='make_single', metavar='name', help='Create a single page file')
		parser.add_argument('--make:taxonomy', dest='make_taxonomy', metavar='name', help='Create a new taxonomy file')
		parser.add_argument('--make:custom_posts', dest='make_customposts', metavar='name', help='Create a new custom post file')
		parser.add_argument('--make:js', dest='make_js', metavar='name', help='Create a new JS file')
		parser.add_argument('--make:ajax', dest='make_ajax', metavar='functionname', help='Create a new AJAX file')
		parser.add_argument('--make:api', dest='make_api', metavar='functionname', help='Create a new API file')		


		parser.add_argument('--acf:global_general', dest='acf_global_general', action='store_true', help='Create ACF file for general (social media, error)')		
		parser.add_argument('--acf:gallery', dest='acf_gallery', action='store_true', help='Create ACF file for Gallery')		
		parser.add_argument('--acf:maps', dest='acf_maps', action='store_true', help='Create ACF files for Maps')		

		parser.add_argument('--build:theme', dest='build_theme', action='store_true', help='Build theme (Starter Theme etc)')
		parser.add_argument('--build:configure_db', dest='configure_db', action='store_true', help='Default configuration for database')


		args = parser.parse_args()
		self.getCommand(args)

	def getCommand(self, args):
		if args.version:
			print('Version: ' + str(app.config['version']))
		if args.make_template:
			template.init(args.make_template)
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
		if args.acf_global_general:
			acf.global_general()
		if args.acf_gallery:
			acf.gallery()
		if args.acf_maps:
			acf.maps()
		if args.build_theme:
			theme.init()
		if args.configure_db:
			db.configure_db()

klein = Kleinisan()