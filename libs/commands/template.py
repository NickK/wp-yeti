#template.py
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	templatename = 'template-' + name
	files = createClass.createClass()
	files.createFile(
		templatename + '.php',
		app.config['folders']['theme_folder'],
		"<?php\n/*\nTemplate Name: " + name[0].upper() + name[1:] + " Template\n*/\n\n\n" +
		"$context = Timber::get_context();\n" +
		"$post = new TimberPost();\n" +
		"$context['post'] = $post;\n" +
		"Timber::render( array( '" + templatename + ".twig' ), $context );"
	)

	files.createFile(
		templatename + '.twig',
		app.config['folders']['views']
	)