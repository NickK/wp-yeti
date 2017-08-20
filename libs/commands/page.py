#template.py
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	pagename = 'page-' + name
	files = createClass.createClass()
	#passing path through is weird
	files.createFile(
		pagename + '.php',
		app.config['folders']['theme_folder'],
		"<?php\n" +
		"$context = Timber::get_context();\n" +
		"$post = new TimberPost();\n" +
		"$context['post'] = $post;\n" +
		"Timber::render( array( '" + pagename + ".twig' ), $context );"
	)

	files.createFile(
		pagename + '.twig',
		app.config['folders']['views']
	)