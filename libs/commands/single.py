#single.py
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	singlename = 'single-' + name
	files = createClass.createClass()
	files.createFile(
		singlename + '.php',
		app.config['folders']['theme_folder'],
		"<?php\n" +
		"$context = Timber::get_context();\n" +
		"$post = Timber::query_post();\n" +
		"$context['post'] = $post;\n" +
		"Timber::render( array( '" + singlename + ".twig', 'single.twig' ), $context );"
	)

	files.createFile(
		singlename + '.twig',
		app.config['folders']['views']
	)