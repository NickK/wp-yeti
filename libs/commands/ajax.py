#template.py
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	files = createClass.createClass()
	#passing path through is weird
	files.createFile(
		name + '.php',
		app.config['folders']['ajax'],
		"<?php\n" +
		"add_action( 'wp_ajax_" + name + "', '" + name + "' );\n"+
		"add_action('wp_ajax_nopriv_"+name+"', '"+name+"' );\n"+
		"function "+name+"() {\n"+
		"	exit;\n"
		"}"
	)