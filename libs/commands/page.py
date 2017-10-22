#page.py
import os
from libs.classes import createFiles as createClass

def init(name):
	#define config vars
	THEME_FOLDER = os.environ.get("THEME_FOLDER")
	VIEWS_FOLDER = os.environ.get("VIEWS_FOLDER")


	pagename = 'page-' + name
	files = createClass.createClass()
	#passing path through is weird
	files.createFile(
		pagename + '.php',
		THEME_FOLDER,
		"<?php\n" +
		"$context = Timber::get_context();\n" +
		"$post = new TimberPost();\n" +
		"$context['post'] = $post;\n" +
		"Timber::render( array( '" + pagename + ".twig' ), $context );"
	)

	files.createFile(
		pagename + '.twig',
		VIEWS_FOLDER
	)