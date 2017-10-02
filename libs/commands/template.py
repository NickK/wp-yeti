#template.py
import os
from libs.classes import createFiles as createClass


class Template:
	def __init__(self, name):
			#define config vars
			THEME_FOLDER = os.environ.get("THEME_FOLDER")
			VIEWS_FOLDER = os.environ.get("VIEWS_FOLDER")


			templatename = 'template-' + name
			files = createClass.createClass()
			files.createFile(
				templatename + '.php',
				THEME_FOLDER,
				"<?php\n/*\nTemplate Name: " + name[0].upper() + name[1:] + " Template\n*/\n\n\n" +
				"$context = Timber::get_context();\n" +
				"$post = new TimberPost();\n" +
				"$context['post'] = $post;\n" +
				"Timber::render( array( '" + templatename + ".twig' ), $context );"
			)

			files.createFile(
				templatename + '.twig',
				VIEWS_FOLDER
			)