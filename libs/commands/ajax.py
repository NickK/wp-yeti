#ajax.py
import os
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	#define config vars	
	AJAX_FOLDER = os.environ.get('AJAX_FOLDER')


	files = createClass.createClass()
	#passing path through is weird
	files.createFile(
		name + '.php',
		AJAX_FOLDER,
		"<?php\n" +
		"add_action( 'wp_ajax_" + name + "', '" + name + "' );\n"+
		"add_action('wp_ajax_nopriv_"+name+"', '"+name+"' );\n"+
		"function "+name+"() {\n"+
		"	exit;\n"
		"}"
	)