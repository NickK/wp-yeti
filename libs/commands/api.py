#template.py
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	files = createClass.createClass()
	#passing path through is weird
	files.createFile(
		name + '.php',
		app.config['folders']['api'],
		"<?php\n" +
		"	header('Content-Type: application/json');\n"
		"	echo json_encode($return);\n"
	)