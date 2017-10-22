#single.py
import os
from libs.classes import createFiles as createClass

def init(name):
	#define config vars	
	THEME_FOLDER = os.environ.get("THEME_FOLDER")
	VIEWS_FOLDER = os.environ.get('VIEWS_FOLDER')

	singlename = 'single-' + name
	files = createClass.createClass()
	files.createFile(
		singlename + '.php',
		THEME_FOLDER,
		"<?php\n" +
		"$context = Timber::get_context();\n" +
		"$post = Timber::query_post();\n" +
		"$context['post'] = $post;\n" +
		"Timber::render( array( '" + singlename + ".twig', 'single.twig' ), $context );"
	)

	files.createFile(
		singlename + '.twig',
		VIEWS_FOLDER
	)